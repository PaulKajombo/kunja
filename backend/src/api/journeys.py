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
from src.core.journey_kb import (
    SUPPORTED_BUSINESS_MODELS,
    SUPPORTED_INDUSTRIES,
    get_business_model_info,
)
from src.core.journey_engine import (
    generate_journey,
    compute_journey_progress,
)
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
def create_journey(data: JourneyCreate, db: Session = Depends(get_db)):
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
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e)) from e

    return _serialize_journey(_get_journey(db, journey.id))


@router.get("")
def list_journeys(db: Session = Depends(get_db)):
    """List all journeys."""
    journeys = (
        db.query(Journey)
        .options(
            selectinload(Journey.phases).selectinload(JourneyPhase.steps)
        )
        .order_by(Journey.created_at.desc())
        .all()
    )
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

    # Build context from the journey
    progress = compute_journey_progress(journey)

    if data.step_id is not None:
        # Find the specific step
        step = None
        phase_name = None
        for phase in journey.phases:
            for s in phase.steps:
                if s.id == data.step_id:
                    step = s
                    phase_name = phase.name
                    break
            if step:
                break

        if not step:
            raise HTTPException(status_code=404, detail="Step not found")

        context = {
            "journey": {
                "company_name": journey.company_name,
                "origin_country": journey.origin_country,
                "target_country": journey.target_country,
                "industry": journey.industry,
                "business_model": journey.business_model,
                "business_description": journey.business_description,
            },
            "step": {
                "title": step.title,
                "phase": phase_name,
                "description": step.description,
                "why_needed": step.why_needed,
                "authority": step.authority,
                "documents_needed": step.documents_needed,
                "instructions": step.instructions,
                "estimated_cost": step.estimated_cost,
                "estimated_timeline": step.estimated_timeline,
                "official_source": step.official_source,
                "status": step.status,
            },
            "question": data.question,
        }
    else:
        # Whole-journey question context
        phase_summaries = []
        for phase in journey.phases:
            steps_summary = [
                {
                    "title": s.title,
                    "status": s.status,
                }
                for s in phase.steps
            ]
            phase_summaries.append(
                {
                    "name": phase.name,
                    "steps": steps_summary,
                }
            )
        context = {
            "journey": {
                "company_name": journey.company_name,
                "origin_country": journey.origin_country,
                "target_country": journey.target_country,
                "industry": journey.industry,
                "business_model": journey.business_model,
                "business_description": journey.business_description,
                "progress": progress,
            },
            "phases": phase_summaries,
            "question": data.question,
        }

    try:
        answer = await ollama_client.ask_about_journey(context)
        return {"answer": answer, "step_id": data.step_id}
    except Exception as e:
        raise HTTPException(
            status_code=503,
            detail=f"Could not reach Ollama. Make sure it's running. Error: {e}",
        ) from e