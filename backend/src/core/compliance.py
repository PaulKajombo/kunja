"""
Kunja compliance knowledge base for Malawi and Zambia.

Each category contains questions the user must answer to assess
compliance for establishing a business in the target country.
"""
from src.core.compliance_mw import MALAWI_QUESTIONS
from src.core.compliance_zm import ZAMBIA_QUESTIONS

COUNTRIES = {
    "malawi": {
        "name": 'Malawi',
        "flag": '🇲🇼',
        "currency": 'Malawi Kwacha (MK)',
        "regulations": MALAWI_QUESTIONS,
    },
    "zambia": {
        "name": 'Zambia',
        "flag": '🇿🇲',
        "currency": 'Zambian Kwacha (ZMW)',
        "regulations": ZAMBIA_QUESTIONS,
    },
}


def get_country_framework(country: str) -> dict | None:
    """Get the compliance framework for a country."""
    return COUNTRIES.get(country.lower())


def calculate_compliance_score(answers: dict, country: str) -> dict:
    """
    Calculate compliance score based on answers.

    Args:
        answers: Dict of {question_id: "yes"/"no"}
        country: "malawi" or "zambia"

    Returns:
        Dict with overall score, category scores, and gap analysis
    """
    framework = get_country_framework(country)
    if not framework:
        return {"error": f"Unknown country: {country}"}

    regulations = framework["regulations"]
    total_weight = 0
    weighted_score = 0
    gaps = []
    category_scores = {}

    for category, category_data in regulations.items():
        cat_weight = category_data["weight"]
        cat_questions = category_data["questions"]
        cat_total = len(cat_questions)
        cat_passed = 0

        for question in cat_questions:
            qid = question["id"]
            answer = answers.get(qid)
            if answer is None:
                continue  # unanswered - don't count

            if answer.lower() in ("yes", "true", "1"):
                cat_passed += 1
            else:
                gaps.append(
                    {
                        "question_id": qid,
                        "category": category,
                        "question": question["question"],
                        "requirement": question["requirement"],
                        "critical": question.get("critical", False),
                        "resource": question.get("resource"),
                    }
                )

        if cat_total > 0:
            cat_score = cat_passed / cat_total
            category_scores[category] = {
                "score": round(cat_score * 100, 1),
                "passed": cat_passed,
                "total": cat_total,
                "name": category_data["name"],
                "regulation": category_data["regulation"],
            }
            total_weight += cat_weight
            weighted_score += cat_score * cat_weight

    overall = round((weighted_score / total_weight) * 100, 1) if total_weight else 0

    return {
        "country": framework["name"],
        "overall_score": overall,
        "category_scores": category_scores,
        "gaps": gaps,
        "critical_gaps": [g for g in gaps if g["critical"]],
        "level": (
            "high" if overall >= 80 else "medium" if overall >= 50 else "low"
        ),
    }