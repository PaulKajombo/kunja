from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from sqlalchemy.orm import Session

from src.database import get_db
from src.core.compliance import (
    get_country_framework,
    calculate_compliance_score,
    COUNTRIES,
)
from src.models.models import Checklist

router = APIRouter()


class ChecklistCreate(BaseModel):
    origin_country: str  # "Malawi" or "Zambia"
    target_country: str  # "Zambia" or "Malawi"
    business_type: str  # "llc", "sole_proprietor", "partnership"
    industry: str
    company_name: str


class AnswerSubmit(BaseModel):
    answers: dict[str, str]  # {question_id: "yes"/"no"}


class ChecklistResponse(BaseModel):
    id: int
    origin_country: str
    target_country: str
    business_type: str
    industry: str
    company_name: str
    compliance_score: Optional[float] = None
    compliance_level: Optional[str] = None
    status: str  # "in_progress", "completed"
    created_at: datetime

    class Config:
        from_attributes = True


@router.get("/countries")
def list_countries():
    """List supported countries and their compliance frameworks."""
    return {
        "countries": [
            {
                "code": code,
                "name": data["name"],
                "flag": data["flag"],
                "categories": [
                    {
                        "key": cat,
                        "name": cat_data["name"],
                        "regulation": cat_data["regulation"],
                        "question_count": len(cat_data["questions"]),
                    }
                    for cat, cat_data in data["regulations"].items()
                ],
            }
            for code, data in COUNTRIES.items()
        ]
    }


@router.get("/questions/{country}")
def get_questions(country: str):
    """Get all compliance questions for a country."""
    framework = get_country_framework(country)
    if not framework:
        raise HTTPException(status_code=404, detail=f"Unknown country: {country}")
    return framework["regulations"]


@router.post("", response_model=ChecklistResponse)
def create_checklist(data: ChecklistCreate, db: Session = Depends(get_db)):
    """Create a new cross-border compliance checklist."""
    if data.origin_country.lower() not in ("malawi", "zambia"):
        raise HTTPException(status_code=400, detail="origin_country must be Malawi or Zambia")
    if data.target_country.lower() not in ("malawi", "zambia"):
        raise HTTPException(status_code=400, detail="target_country must be Malawi or Zambia")
    if data.origin_country.lower() == data.target_country.lower():
        raise HTTPException(status_code=400, detail="origin and target must be different")

    checklist = Checklist(
        origin_country=data.origin_country,
        target_country=data.target_country,
        business_type=data.business_type,
        industry=data.industry,
        company_name=data.company_name,
        status="in_progress",
        answers={},
        gap_analysis=[],
    )
    db.add(checklist)
    db.commit()
    db.refresh(checklist)
    return checklist


@router.get("/{checklist_id}", response_model=ChecklistResponse)
def get_checklist(checklist_id: int, db: Session = Depends(get_db)):
    """Get a compliance checklist by ID."""
    checklist = db.query(Checklist).filter(Checklist.id == checklist_id).first()
    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist not found")
    return checklist


@router.get("")
def list_checklists(origin: str = None, target: str = None, db: Session = Depends(get_db)):
    """List all checklists, optionally filtered by origin/target country."""
    query = db.query(Checklist)
    if origin:
        query = query.filter(Checklist.origin_country.ilike(f"%{origin}%"))
    if target:
        query = query.filter(Checklist.target_country.ilike(f"%{target}%"))
    checklists = query.order_by(Checklist.created_at.desc()).all()
    return {"checklists": checklists, "total": len(checklists)}


@router.post("/{checklist_id}/submit")
def submit_answers(
    checklist_id: int, data: AnswerSubmit, db: Session = Depends(get_db)
):
    """Submit answers and compute compliance score."""
    checklist = db.query(Checklist).filter(Checklist.id == checklist_id).first()
    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist not found")

    # Compute compliance against the TARGET country framework
    result = calculate_compliance_score(data.answers, checklist.target_country)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    checklist.answers = data.answers
    checklist.gap_analysis = result["gaps"]
    checklist.compliance_score = result["overall_score"]
    checklist.compliance_level = result["level"]
    checklist.status = "completed"
    db.commit()
    db.refresh(checklist)

    return {
        "checklist_id": checklist_id,
        "compliance_score": result["overall_score"],
        "compliance_level": result["level"],
        "category_scores": result["category_scores"],
        "gaps": result["gaps"],
        "critical_gaps_count": len(result["critical_gaps"]),
        "status": "completed",
    }


@router.get("/{checklist_id}/results")
def get_results(checklist_id: int, db: Session = Depends(get_db)):
    """Get stored results for a completed checklist."""
    checklist = db.query(Checklist).filter(Checklist.id == checklist_id).first()
    if not checklist:
        raise HTTPException(status_code=404, detail="Checklist not found")

    if checklist.status != "completed" or checklist.compliance_score is None:
        raise HTTPException(status_code=400, detail="Checklist not yet completed")

    # Recompute category scores from stored answers
    result = calculate_compliance_score(checklist.answers or {}, checklist.target_country)

    return {
        "checklist_id": checklist_id,
        "company_name": checklist.company_name,
        "target_country": checklist.target_country,
        "origin_country": checklist.origin_country,
        "compliance_score": checklist.compliance_score,
        "compliance_level": checklist.compliance_level,
        "category_scores": result["category_scores"],
        "gaps": checklist.gap_analysis or [],
        "critical_gaps_count": len([g for g in (checklist.gap_analysis or []) if g.get("critical")]),
        "status": "completed",
    }
