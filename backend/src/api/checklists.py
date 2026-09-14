from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

router = APIRouter()


class ChecklistCreate(BaseModel):
    origin_country: str  # "Malawi" or "Zambia"
    target_country: str  # "Zambia" or "Malawi"
    business_type: str  # "llc", "sole_proprietor", "partnership"
    industry: str
    company_name: str


class ChecklistResponse(BaseModel):
    id: str
    origin_country: str
    target_country: str
    business_type: str
    industry: str
    company_name: str
    compliance_score: Optional[float] = None
    status: str  # "in_progress", "completed"
    created_at: datetime


# In-memory store for MVP
checklists_db: dict[str, dict] = {}


@router.post("", response_model=ChecklistResponse)
def create_checklist(data: ChecklistCreate):
    """Create a new cross-border compliance checklist."""
    import uuid
    checklist_id = str(uuid.uuid4())[:8]
    checklist = {
        "id": checklist_id,
        "origin_country": data.origin_country,
        "target_country": data.target_country,
        "business_type": data.business_type,
        "industry": data.industry,
        "company_name": data.company_name,
        "compliance_score": None,
        "status": "in_progress",
        "created_at": datetime.now(),
    }
    checklists_db[checklist_id] = checklist
    return checklist


@router.get("/{checklist_id}", response_model=ChecklistResponse)
def get_checklist(checklist_id: str):
    """Get a compliance checklist by ID."""
    checklist = checklists_db.get(checklist_id)
    if not checklist:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Checklist not found")
    return checklist


@router.get("")
def list_checklists(origin: str = None, target: str = None):
    """List all checklists, optionally filtered by origin/target country."""
    results = list(checklists_db.values())
    if origin:
        results = [c for c in results if c["origin_country"].lower() == origin.lower()]
    if target:
        results = [c for c in results if c["target_country"].lower() == target.lower()]
    return {"checklists": results, "total": len(results)}
