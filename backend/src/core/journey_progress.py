"""
Journey progress computation.

Kept separate from the generation engine so each module stays small.
"""

from src.models.models import Journey


def compute_journey_progress(journey: Journey) -> dict:
    """Compute progress statistics for a journey."""
    total_steps = 0
    completed_steps = 0
    in_progress_steps = 0
    blocked_steps = 0

    for phase in journey.phases:
        for step in phase.steps:
            total_steps += 1
            if step.status == "completed":
                completed_steps += 1
            elif step.status == "in_progress":
                in_progress_steps += 1
            elif step.status == "blocked":
                blocked_steps += 1

    percentage = (
        round((completed_steps / total_steps) * 100) if total_steps > 0 else 0
    )

    # Find next actionable step
    next_step = None
    for phase in journey.phases:
        for step in phase.steps:
            if step.status in ("not_started", "in_progress"):
                next_step = step
                break
        if next_step:
            break

    return {
        "total_steps": total_steps,
        "completed_steps": completed_steps,
        "in_progress_steps": in_progress_steps,
        "blocked_steps": blocked_steps,
        "percentage": percentage,
        "next_step_id": next_step.id if next_step else None,
        "next_step_title": next_step.title if next_step else None,
    }