from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter()


class Regulation(BaseModel):
    id: str
    country: str
    name: str
    chapter: str
    summary: str
    category: str  # "business_registration", "tax", "employment", "data_protection", "immigration"


MALAWI_REGULATIONS = [
    {
        "id": "mw-companies-act",
        "country": "Malawi",
        "name": "Companies Act",
        "chapter": "Chapter 49:03",
        "summary": "Business registration, directors duties, filing requirements",
        "category": "business_registration",
    },
    {
        "id": "mw-income-tax-act",
        "country": "Malawi",
        "name": "Income Tax Act",
        "chapter": "Chapter 44:06",
        "summary": "Corporate tax, VAT, PAYE, tax filings",
        "category": "tax",
    },
    {
        "id": "mw-data-protection-act",
        "country": "Malawi",
        "name": "Data Protection Act",
        "chapter": "Chapter 4:10",
        "summary": "Data protection compliance (2021 Act)",
        "category": "data_protection",
    },
    {
        "id": "mw-employment-act",
        "country": "Malawi",
        "name": "Employment Act",
        "chapter": "Chapter 4:03",
        "summary": "Labour laws, contracts, termination, benefits",
        "category": "employment",
    },
    {
        "id": "mw-immigration-act",
        "country": "Malawi",
        "name": "Immigration Act",
        "chapter": "Chapter 15:08",
        "summary": "Work permits for foreign nationals (Zambians)",
        "category": "immigration",
    },
    {
        "id": "mw-vat-act",
        "country": "Malawi",
        "name": "Value Added Tax Act",
        "chapter": "Chapter 4:05",
        "summary": "VAT registration and compliance",
        "category": "tax",
    },
]

ZAMBIA_REGULATIONS = [
    {
        "id": "zm-companies-act",
        "country": "Zambia",
        "name": "Companies Act No. 10 of 2017",
        "chapter": "Act No. 10 of 2017",
        "summary": "Business registration, directors duties",
        "category": "business_registration",
    },
    {
        "id": "zm-income-tax-act",
        "country": "Zambia",
        "name": "Income Tax Act No. 12 of 2015",
        "chapter": "Act No. 12 of 2015",
        "summary": "Corporate tax, VAT, PAYE",
        "category": "tax",
    },
    {
        "id": "zm-data-protection-act",
        "country": "Zambia",
        "name": "Data Protection Act No. 3 of 2021",
        "chapter": "Act No. 3 of 2021",
        "summary": "Data protection compliance",
        "category": "data_protection",
    },
    {
        "id": "zm-employment-code-act",
        "country": "Zambia",
        "name": "Employment Code Act No. 3 of 2019",
        "chapter": "Act No. 3 of 2019",
        "summary": "Labour laws, contracts, termination",
        "category": "employment",
    },
    {
        "id": "zm-immigration-act",
        "country": "Zambia",
        "name": "Immigration and Deportation Act",
        "chapter": "Cap 123",
        "summary": "Work permits for foreign nationals (Malawians)",
        "category": "immigration",
    },
    {
        "id": "zm-vat-act",
        "country": "Zambia",
        "name": "VAT Act No. 12 of 2018",
        "chapter": "Act No. 12 of 2018",
        "summary": "VAT registration and compliance",
        "category": "tax",
    },
    {
        "id": "zm-ceea",
        "country": "Zambia",
        "name": "Citizens Economic Empowerment Act",
        "chapter": "Cap 254",
        "summary": "Local ownership requirements",
        "category": "business_registration",
    },
]


@router.get("/malawi")
def list_malawi_regulations():
    """List all Malawi regulations."""
    return {"country": "Malawi", "regulations": MALAWI_REGULATIONS, "total": len(MALAWI_REGULATIONS)}


@router.get("/zambia")
def list_zambia_regulations():
    """List all Zambia regulations."""
    return {"country": "Zambia", "regulations": ZAMBIA_REGULATIONS, "total": len(ZAMBIA_REGULATIONS)}


@router.get("/{country}/{regulation_id}")
def get_regulation(country: str, regulation_id: str):
    """Get a specific regulation by ID."""
    all_regs = MALAWI_REGULATIONS + ZAMBIA_REGULATIONS
    for reg in all_regs:
        if reg["id"] == regulation_id:
            return reg
    from fastapi import HTTPException
    raise HTTPException(status_code=404, detail="Regulation not found")
