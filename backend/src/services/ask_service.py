"""
Ask-Kunja service: builds grounded context from a journey and answers,
falling back to the structured knowledge base when the LLM is offline.
"""

from fastapi import HTTPException

from src.models.models import Journey


def _journey_profile(journey: Journey) -> dict:
    return {
        "company_name": journey.company_name,
        "origin_country": journey.origin_country,
        "target_country": journey.target_country,
        "industry": journey.industry,
        "business_model": journey.business_model,
        "business_description": journey.business_description,
    }


def build_step_context(journey: Journey, step_id: int, question: str) -> dict:
    step = None
    phase_name = None
    for phase in journey.phases:
        for s in phase.steps:
            if s.id == step_id:
                step = s
                phase_name = phase.name
                break
        if step:
            break
    if not step:
        raise HTTPException(status_code=404, detail="Step not found")

    return {
        "journey": _journey_profile(journey),
        "question": question,
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
            "user_notes": step.user_notes,
        },
    }


def build_journey_context(journey: Journey, question: str, progress: dict) -> dict:
    phase_summaries = [
        {
            "name": phase.name,
            "steps": [
                {"title": s.title, "status": s.status} for s in phase.steps
            ],
        }
        for phase in journey.phases
    ]
    profile = _journey_profile(journey)
    profile["progress"] = progress
    return {
        "journey": profile,
        "phases": phase_summaries,
        "question": question,
    }


def grounded_fallback(context: dict) -> str:
    """Answer directly from the structured knowledge base (no LLM needed)."""
    if "step" in context:
        s = context["step"]
        lines = [f"**{s.get('title', 'Step')}**"]
        if s.get("phase"):
            lines.append(f"Phase: {s['phase']}")
        if s.get("description"):
            lines.append(f"\n{s['description']}")
        if s.get("why_needed"):
            lines.append(f"\n**Why needed:** {s['why_needed']}")
        if s.get("authority"):
            lines.append(f"\n**Responsible authority:** {s['authority']}")
        docs = s.get("documents_needed") or []
        if docs:
            lines.append("\n**Documents needed:**\n- " + "\n- ".join(docs))
        if s.get("instructions"):
            lines.append(f"\n**How to do it:**\n{s['instructions']}")
        if s.get("estimated_cost"):
            lines.append(f"\n**Estimated cost:** {s['estimated_cost']}")
        if s.get("estimated_timeline"):
            lines.append(f"\n**Estimated timeline:** {s['estimated_timeline']}")
        if s.get("official_source"):
            lines.append(f"\n**Official source:** {s['official_source']}")
        lines.append(
            "\n_(Source: Kunja market-entry knowledge base. The AI assistant is "
            "offline, so this comes from the structured roadmap.)_"
        )
        return "\n".join(lines)

    j = context.get("journey", {})
    lines = [
        f"**{j.get('company_name', 'Your business')}** — "
        f"{j.get('origin_country', '?')} → {j.get('target_country', '?')}",
        f"Industry: {j.get('industry', 'N/A')} · "
        f"Model: {j.get('business_model', 'N/A')}",
    ]
    progress = j.get("progress") or context.get("progress")
    if progress:
        lines.append(
            f"Progress: {progress.get('completed_steps', 0)} of "
            f"{progress.get('total_steps', 0)} steps complete "
            f"({progress.get('percentage', 0)}%)"
        )
    for phase in context.get("phases", []):
        steps = "; ".join(
            f"{s['title']} ({s['status']})" for s in phase.get("steps", [])
        )
        lines.append(f"\n**{phase.get('name', 'Phase')}:** {steps}")
    lines.append(
        "\n_(Source: Kunja market-entry knowledge base. The AI assistant is "
        "offline, so this is a summary of your roadmap.)_"
    )
    return "\n".join(lines)