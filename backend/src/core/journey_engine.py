"""
Journey Generation Engine for Kunja.

Takes a user profile (origin, target, industry, business model)
and generates a concrete Journey with Phases and Steps
from the knowledge base, applying industry and business-model modifiers.
"""

from sqlalchemy.orm import Session

from src.models.models import Journey, JourneyPhase, JourneyStep
from src.core.journey_kb import (
    get_journey_template,
    INDUSTRY_MODIFIERS,
)
from src.core.journey_progress import compute_journey_progress


def _slug(title: str) -> str:
    """Convert a step title to a machine-readable slug (fallback)."""
    return (
        title.lower()
        .replace("(", "")
        .replace(")", "")
        .replace("/", "_")
        .replace(" ", "_")
        .replace("-", "_")
        .replace(",", "")
        .replace("'", "")
        .replace('"', "")
    )


def _step_slug(step: dict) -> str:
    """Return the step's canonical slug, preferring an explicit one.

    The knowledge base defines stable slugs per step so that dependency
    references and industry/business-model modifiers don't break when a
    title is edited for display.
    """
    return step.get("slug") or _slug(step["title"])


def _pair_key(origin: str, target: str) -> str:
    return f"{origin.lower()}_{target.lower()}"


def _filter_steps_by_business_model(
    steps: list[dict], business_model: str
) -> list[dict]:
    """Keep only steps that apply to the given business model.

    Each step can declare ``business_models`` (e.g. ["branch", "subsidiary"]).
    Steps without the field apply to every model.
    """
    filtered = []
    for step in steps:
        allowed_models = step.get("business_models")
        if allowed_models and business_model not in allowed_models:
            continue
        filtered.append(step)
    return filtered


def _apply_industry_modifiers(
    phases: list[dict], industry: str, origin: str, target: str
) -> list[dict]:
    """Add or remove steps based on the user's industry.

    Modifiers are looked up per country pair so the same industry can
    behave differently in each direction (e.g. Zambia's phytosanitary
    authority differs from Malawi's).
    """
    pair = _pair_key(origin, target)
    modifier = INDUSTRY_MODIFIERS.get(pair, {}).get(industry, {})
    extra_steps = modifier.get("extra_steps", {})
    remove_slugs = set(modifier.get("remove_steps", []))

    for phase in phases:
        phase_num = phase["phase_number"]

        if remove_slugs:
            phase["steps"] = [
                s for s in phase["steps"] if _step_slug(s) not in remove_slugs
            ]

        if phase_num in extra_steps:
            phase["steps"].extend(extra_steps[phase_num])

    return phases


def _resolve_depends_on(
    depends_on: list[str], slug_map: dict[str, int]
) -> list[int]:
    """Convert dependency slugs to step IDs. Returns empty list if deps not found."""
    resolved = []
    for dep_slug in depends_on:
        if dep_slug in slug_map:
            resolved.append(slug_map[dep_slug])
    return resolved


def generate_journey(
    db: Session,
    company_name: str,
    origin_country: str,
    target_country: str,
    industry: str,
    business_model: str,
    business_description: str = None,
    user_id: int | None = None,
) -> Journey:
    """
    Generate a complete Journey from the knowledge base.

    1. Load the template for this country pair
    2. Apply industry modifiers (add/remove steps)
    3. Filter steps by business model
    4. Persist to database and resolve dependencies
    5. Return the populated Journey object
    """
    template = get_journey_template(origin_country, target_country)
    if not template:
        raise ValueError(
            f"No journey template for {origin_country} → {target_country}"
        )

    # Create the Journey record
    journey = Journey(
        user_id=user_id,
        company_name=company_name,
        origin_country=origin_country,
        target_country=target_country,
        industry=industry,
        business_model=business_model,
        business_description=business_description,
        status="in_progress",
    )
    db.add(journey)
    db.flush()  # get the journey.id

    # Build all phases
    slug_to_id: dict[str, int] = {}  # slug → step.id (for dependency resolution)

    for phase_data in template["phases"]:
        # Apply industry modifiers
        phases_with_industry = _apply_industry_modifiers(
            [phase_data], industry, origin_country, target_country
        )
        phase_data = phases_with_industry[0]

        # Filter steps by business model
        filtered_steps = _filter_steps_by_business_model(
            phase_data["steps"], business_model
        )

        if not filtered_steps:
            continue  # skip empty phases

        # Create phase
        phase = JourneyPhase(
            journey_id=journey.id,
            phase_number=phase_data["phase_number"],
            name=phase_data["name"],
            description=phase_data["description"],
        )
        db.add(phase)
        db.flush()

        # Create steps
        for step_num, step_data in enumerate(filtered_steps):
            step_slug = _step_slug(step_data)

            step = JourneyStep(
                phase_id=phase.id,
                step_number=step_num + 1,
                title=step_data["title"],
                slug=step_slug,
                description=step_data.get("description"),
                why_needed=step_data.get("why_needed"),
                authority=step_data.get("authority"),
                documents_needed=step_data.get("documents_needed", []),
                instructions=step_data.get("instructions"),
                estimated_cost=step_data.get("estimated_cost"),
                estimated_timeline=step_data.get("estimated_timeline"),
                official_source=step_data.get("official_source"),
                depends_on=step_data.get("depends_on", []),
                status="not_started",
            )

            db.add(step)
            db.flush()
            slug_to_id[step_slug] = step.id

    # Second pass: resolve dependencies to step IDs
    # (we store both slugs for display and resolved IDs for logic)
    all_steps = (
        db.query(JourneyStep)
        .join(JourneyPhase)
        .filter(JourneyPhase.journey_id == journey.id)
        .all()
    )

    for step in all_steps:
        if step.depends_on:
            resolved = _resolve_depends_on(step.depends_on, slug_to_id)
            step.depends_on = resolved
            # Check if any dependency is not completed → block this step
            if resolved:
                dep_statuses = (
                    db.query(JourneyStep.id, JourneyStep.status)
                    .filter(JourneyStep.id.in_(resolved))
                    .all()
                )
                if any(status != "completed" for _, status in dep_statuses):
                    step.status = "blocked"

    db.commit()
    db.refresh(journey)
    return journey