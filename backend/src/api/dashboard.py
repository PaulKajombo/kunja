from fastapi import APIRouter

router = APIRouter()


@router.get("/compliance-score")
def get_compliance_score():
    """Get overall compliance score for both countries."""
    return {
        "malawi": {
            "score": 0,
            "status": "no_data",
            "checks_completed": 0,
            "checks_total": 0,
        },
        "zambia": {
            "score": 0,
            "status": "no_data",
            "checks_completed": 0,
            "checks_total": 0,
        },
        "overall": 0.0,
        "message": "Complete a compliance checklist to see your score",
    }


@router.get("/timeline")
def get_timeline():
    """Get compliance activity timeline."""
    return {
        "timeline": [],
        "message": "No activity yet - start a compliance checklist",
    }
