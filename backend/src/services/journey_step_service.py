"""
Step-level business rules for journeys.

Handles status validation, dependency enforcement, unblocking, and
auto-completion of the parent journey.
"""

from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.models.models import Journey, JourneyPhase, JourneyStep


VALID_STATUSES = {"not_started", "in_progress", "completed", "skipped"}


def validate_status(status: str) -> None:
    if status not in VALID_STATUSES:
        raise HTTPException(
            status_code=400,
            detail=f"status must be one of: {sorted(VALID_STATUSES)}",
        )


def validate_step_deps(db: Session, step: JourneyStep) -> None:
    """Check that a step's dependencies are met before marking it completed."""
    if not step.depends_on:
        return
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


def unblock_ready_steps(db: Session, journey_id: int) -> None:
    """
    After a step is marked completed, promote any blocked steps
    whose own dependencies have all been satisfied.
    """
    all_steps = (
        db.query(JourneyStep)
        .join(JourneyPhase, JourneyStep.phase_id == JourneyPhase.id)
        .filter(JourneyPhase.journey_id == journey_id)
        .all()
    )
    step_ids = {s.id for s in all_steps}

    for s in all_steps:
        if s.status != "blocked":
            continue
        deps = [d for d in (s.depends_on or []) if d in step_ids]
        dep_statuses = {
            sid: st
            for sid, st in db.query(JourneyStep.id, JourneyStep.status)
            .filter(JourneyStep.id.in_(deps))
            .all()
        }
        if all(dep_statuses.get(d) == "completed" for d in deps):
            s.status = "not_started"


def auto_complete_if_done(db: Session, journey: Journey) -> bool:
    """
    Mark the journey completed if every step is done.

    Returns True if the journey was just completed.
    """
    all_steps = (
        db.query(JourneyStep)
        .join(JourneyPhase, JourneyStep.phase_id == JourneyPhase.id)
        .filter(JourneyPhase.journey_id == journey.id)
        .all()
    )
    if all_steps and all(s.status == "completed" for s in all_steps):
        journey.status = "completed"
        return True
    return False


def apply_step_update(
    db: Session,
    journey_id: int,
    step: JourneyStep,
    status: str,
    user_notes: str | None = None,
) -> None:
    """
    Apply a step update: validate, set fields, unblock dependants,
    and auto-complete the journey if all steps are done.
    """
    validate_status(status)
    validate_step_deps(db, step)

    step.status = status
    if user_notes is not None:
        step.user_notes = user_notes
    db.commit()

    if status == "completed":
        unblock_ready_steps(db, journey_id)
        journey = db.query(Journey).get(journey_id)
        auto_complete_if_done(db, journey)
        db.commit()
