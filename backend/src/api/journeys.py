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
from src.models.models import User
from src.services.auth_service import get_optional_user
from src.core.journey_kb import (
    SUPPORTED_BUSINESS_MODELS,
    SUPPORTED_INDUSTRIES,
    get_business_model_info,
)
from src.core.journey_engine import (
    generate_journey,
    compute_journey_progress,
)
from src.services import ask_service
from src.models.models import Journey, JourneyPhase, JourneyStep
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


def _serialize_journey(journey: Journey) -> dict:
    """Serialize a Journey with all phases and steps."""
    progress = compute_journey_progress(journey)
    model_info = get_business_model_info(journey.business_model)

    phases = []
    for phase in journey.phases:
        steps = []
        for step in phase.steps:
            steps.append(
                {
                    "id": step.id,
                    "step_number": step.step_number,
                    "title": step.title,
                    "slug": step.slug,
                    "description": step.description,
                    "why_needed": step.why_needed,
                    "authority": step.authority,
                    "documents_needed": step.documents_needed,
                    "instructions": step.instructions,
                    "estimated_cost": step.estimated_cost,
                    "estimated_timeline": step.estimated_timeline,
                    "official_source": step.official_source,
                    "status": step.status,
                    "user_notes": step.user_notes,
                    "depends_on": step.depends_on,
                }
            )
        phases.append(
            {
                "id": phase.id,
                "phase_number": phase.phase_number,
                "name": phase.name,
                "description": phase.description,
                "steps": steps,
            }
        )

    return {
        "id": journey.id,
        "company_name": journey.company_name,
        "origin_country": journey.origin_country,
        "target_country": journey.target_country,
        "industry": journey.industry,
        "business_model": journey.business_model,
        "business_model_label": model_info.get("label", journey.business_model),
        "business_description": journey.business_description,
        "status": journey.status,
        "created_at": journey.created_at.isoformat() if journey.created_at else None,
        "phases": phases,
        "progress": progress,
    }


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

    return _serialize_journey(_get_journey(db, journey.id))


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
        "journeys": [_serialize_journey(j) for j in journeys],
        "total": len(journeys),
    }


@router.get("/{journey_id}")
def get_journey(journey_id: int, db: Session = Depends(get_db)):
    """Get a journey with all phases, steps, and progress."""
    journey = _get_journey(db, journey_id)
    return _serialize_journey(journey)


@router.patch("/{journey_id}/steps/{step_id}")
def update_step(
    journey_id: int,
    step_id: int,
    data: StepUpdate,
    db: Session = Depends(get_db),
):
    """Update a step's status and notes."""
    journey = _get_journey(db, journey_id)

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

    valid_statuses = {"not_started", "in_progress", "completed", "skipped"}
    if data.status not in valid_statuses:
        raise HTTPException(
            status_code=400,
            detail=f"status must be one of: {sorted(valid_statuses)}",
        )

    # Check dependencies are met before allowing 'completed'
    if data.status == "completed" and step.depends_on:
        dep_steps = (
            db.query(JourneyStep.id, JourneyStep.status)
            .filter(JourneyStep.id.in_(step.depends_on))
            .all()
        )
        unsatisfied = [sid for sid, s in dep_steps if s != "completed"]
        if unsatisfied:
            raise HTTPException(
                status_code=400,
                detail="Cannot complete this step — its prerequisites are not done yet.",
            )

    step.status = data.status
    if data.user_notes is not None:
        step.user_notes = data.user_notes

    db.commit()

    # Unblock any steps that were blocked on this step
    if data.status == "completed":
        all_steps = (
            db.query(JourneyStep)
            .join(JourneyPhase, JourneyStep.phase_id == JourneyPhase.id)
            .filter(JourneyPhase.journey_id == journey_id)
            .all()
        )
        step_ids = {s.id for s in all_steps}
        for s in all_steps:
            if s.status == "blocked":
                deps = [d for d in (s.depends_on or []) if d in step_ids]
                dep_statuses = {
                    sid: st
                    for sid, st in db.query(
                        JourneyStep.id, JourneyStep.status
                    )
                    .filter(JourneyStep.id.in_(deps))
                    .all()
                }
                if all(dep_statuses.get(d) == "completed" for d in deps):
                    s.status = "not_started"

        # Auto-complete the journey when every step is done
        if all_steps and all(s.status == "completed" for s in all_steps):
            journey.status = "completed"
        db.commit()

    return _serialize_journey(_get_journey(db, journey_id))


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