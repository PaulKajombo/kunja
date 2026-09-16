"""
Journey serialization.

Keeps the response-shape logic in one place so that API routers and
background tasks can reuse a canonical representation.
"""

from src.models.models import Journey
from src.core.journey_kb import get_business_model_info
from src.core.journey_engine import compute_journey_progress


def serialize_journey(journey: Journey) -> dict:
    """Serialize a Journey with all phases and steps."""
    progress = compute_journey_progress(journey)
    model_info = get_business_model_info(journey.business_model)

    phases = []
    for phase in journey.phases:
        steps = [
            {
                "id": s.id,
                "step_number": s.step_number,
                "title": s.title,
                "slug": s.slug,
                "description": s.description,
                "why_needed": s.why_needed,
                "authority": s.authority,
                "documents_needed": s.documents_needed,
                "instructions": s.instructions,
                "estimated_cost": s.estimated_cost,
                "estimated_timeline": s.estimated_timeline,
                "official_source": s.official_source,
                "status": s.status,
                "user_notes": s.user_notes,
                "depends_on": s.depends_on,
            }
            for s in phase.steps
        ]
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
