"""
Journey API endpoints for Kunja.

Endpoints:
    GET  /api/v1/journeys/options      -> supported countries, industries, business models
    POST /api/v1/journeys              -> create a journey from user profile
    GET  /api/v1/journeys              -> list all journeys
    GET  /api/v1/journeys/{id}         -> full journey with phases + steps
    PATCH /api/v1/journeys/{id}/steps/{step_id} -> update step status
    POST /api/v1/journeys/{id}/ask     -> ask Kunja about a specific step
    POST /api/v1/journeys/{id}/ask-all -> ask Kunja about the whole journey
"""

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session, selectinload

from src.database import get_db
from src.models.models import User, Journey, JourneyPhase, JourneyStep
from src.services.auth_service import get_optional_user
from src.services import ask_service, journey_step_service
from src.services.serializers import serialize_journey
from src.core.journey_kb import (
    SUPPORTED_BUSINESS_MODELS,
    SUPPORTED_INDUSTRIES,
)
from src.core.journey_engine import (
    generate_journey,
    compute_journey_progress,
)
from src.ai import ollama_client


router = APIRouter()


# ─────────────────────────────────────────────
# Pydantic Schemas
# ─────────────────────────────────────────────


class JourneyCreate(BaseModel):
    company_name: str
    origin_country: str  # "malawi" or "zambia"
    target_country: str  # "zambia" or "malawi"
    industry: str  # "agriculture", "technology", etc.
    business_model: str  # "export", "distributor", "agent", "branch", "subsidiary"
    business_description: Optional[str] = None


class StepUpdate(BaseModel):
    status: str  # not_started, in_progress, completed, skipped
    user_notes: Optional[str] = None


class AskRequest(BaseModel):
    step_id: Optional[int] = None  # If None, asks about the whole journey
    question: str


# ─────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────


def _get_journey(db: Session, journey_id: int) -> Journey:
    """Load a journey with all relationships eagerly."""
    journey = (
        db.query(Journey)
        .options(
            selectinload(Journey.phases).selectinload(JourneyPhase.steps)
        )
        .filter(Journey.id == journey_id)
        .first()
    )
    if not journey:
        raise HTTPException(status_code=404, detail="Journey not found")
    return journey


# ─────────────────────────────────────────────
# Endpoints
# ─────────────────────────────────────────────


@router.get("/options")
def get_options():
    """Get the supported configuration options."""
    return {
        "countries": [
            {"key": "malawi", "name": "Malawi", "flag": "🇲🇼"},
            {"key": "zambia", "name": "Zambia", "flag": "🇿🇲"},
        ],
        "industries": SUPPORTED_INDUSTRIES,
        "business_models": SUPPORTED_BUSINESS_MODELS,
    }


@router.post("", status_code=201)
def create_journey(
    data: JourneyCreate,
    db: Session = Depends(get_db),
    user: User | None = Depends(get_optional_user),
):
    """Create a new market-entry journey."""
    # Validate countries
    if data.origin_country not in ("malawi", "zambia"):
        raise HTTPException(status_code=400, detail="origin_country must be 'malawi' or 'zambia'")
    if data.target_country not in ("malawi", "zambia"):
        raise HTTPException(status_code=400, detail="target_country must be 'zambia' or 'malawi'")
    if data.origin_country == data.target_country:
        raise HTTPException(status_code=400, detail="origin and target must be different")

    # Validate business model
    valid_models = {m["key"] for m in SUPPORTED_BUSINESS_MODELS}
    if data.business_model not in valid_models:
        raise HTTPException(
            status_code=400,
            detail=f"business_model must be one of: {sorted(valid_models)}",
        )

    try:
        journey = generate_journey(
            db=db,
            company_name=data.company_name,
            origin_country=data.origin_country,
            target_country=data.target_country,
            industry=data.industry,
            business_model=data.business_model,
            business_description=data.business_description,
            user_id=user.id if user else None,
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return serialize_journey(_get_journey(db, journey.id))


@router.get("")
def list_journeys(db: Session = Depends(get_db), user: User | None = Depends(get_optional_user)):
    """List journeys. When authenticated, only the caller's journeys are returned."""
    query = db.query(Journey)
    if user is not None:
        query = query.filter(Journey.user_id == user.id)
    journeys = query.options(
            selectinload(Journey.phases).selectinload(JourneyPhase.steps)
        ).order_by(Journey.created_at.desc()).all()
    return {
        "journeys": [serialize_journey(j) for j in journeys],
        "total": len(journeys),
    }


@router.get("/{journey_id}")
def get_journey(journey_id: int, db: Session = Depends(get_db)):
    """Get a journey with all phases, steps, and progress."""
    journey = _get_journey(db, journey_id)
    return serialize_journey(journey)


@router.patch("/{journey_id}/steps/{step_id}")
def update_step(
    journey_id: int,
    step_id: int,
    data: StepUpdate,
    db: Session = Depends(get_db),
):
    """Update a step's status and notes."""
    _get_journey(db, journey_id)

    step = (
        db.query(JourneyStep)
        .join(JourneyPhase, JourneyStep.phase_id == JourneyPhase.id)
        .filter(
            JourneyStep.id == step_id,
            JourneyPhase.journey_id == journey_id,
        )
        .first()
    )
    if not step:
        raise HTTPException(status_code=404, detail="Step not found in this journey")

    journey_step_service.apply_step_update(
        db=db,
        journey_id=journey_id,
        step=step,
        status=data.status,
        user_notes=data.user_notes,
    )

    return serialize_journey(_get_journey(db, journey_id))


@router.post("/{journey_id}/ask")
async def ask_kunja(
    journey_id: int,
    data: AskRequest,
    db: Session = Depends(get_db),
):
    """Ask Kunja (Ollama) about a specific step or the whole journey."""
    journey = _get_journey(db, journey_id)
    if not data.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    if data.step_id is not None:
        context = ask_service.build_step_context(journey, data.step_id, data.question)
    else:
        progress = compute_journey_progress(journey)
        context = ask_service.build_journey_context(journey, data.question, progress)

    try:
        answer = await ollama_client.ask_about_journey(context)
        return {"answer": answer, "step_id": data.step_id}
    except Exception:
        # Grounded fallback: answer from the structured KB instead of a 503
        return {
            "answer": ask_service.grounded_fallback(context),
            "step_id": data.step_id,
            "mode": "kb",
        }