from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.models import Checklist

router = APIRouter()


@router.get("/compliance-score")
def get_compliance_score(db: Session = Depends(get_db)):
    """Get overall compliance score for both countries."""
    checklists = db.query(Checklist).all()
    completed = [c for c in checklists if c.status == "completed"]

    scores = {
        "malawi": {"score": 0, "checks_completed": 0, "checks_total": 0},
        "zambia": {"score": 0, "checks_completed": 0, "checks_total": 0},
    }

    for c in completed:
        target = c.target_country.lower()
        if target in scores:
            scores[target]["checks_completed"] += 1
            scores[target]["score"] = c.compliance_score or 0

    avg_scores = []
    for country in scores.values():
        if country["checks_completed"] > 0:
            country["average_score"] = round(country["score"] / country["checks_completed"], 1)
            avg_scores.append(country["average_score"])
        else:
            country["average_score"] = None

    overall = round(sum(avg_scores) / len(avg_scores), 1) if avg_scores else 0

    return {
        "malawi": scores["malawi"],
        "zambia": scores["zambia"],
        "overall": overall,
        "total_checklists": len(checklists),
        "completed_checklists": len(completed),
        "message": "Complete a compliance checklist to see your score" if not completed else None,
    }


@router.get("/timeline")
def get_timeline(db: Session = Depends(get_db)):
    """Get compliance activity timeline."""
    checklists = db.query(Checklist).order_by(Checklist.created_at.desc()).all()
    timeline = [
        {
            "id": c.id,
            "company": c.company_name,
            "action": f"Compliance checklist {'completed' if c.status == 'completed' else 'created'}",
            "target_country": c.target_country,
            "compliance_score": c.compliance_score,
            "date": c.updated_at if c.status == "completed" else c.created_at,
        }
        for c in checklists
    ]
    return {"timeline": timeline, "total": len(timeline)}
