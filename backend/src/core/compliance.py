"""
Kunja compliance knowledge base for Malawi and Zambia.

Each category contains questions the user must answer to assess
compliance for establishing a business in the target country.
"""

# ---------------------------------------------------------------------------
# MALAWI COMPLIANCE QUESTIONS
# Target: Zambians expanding into Malawi
# ---------------------------------------------------------------------------

MALAWI_QUESTIONS = {
    "business_registration": {
        "name": "Business Registration",
        "regulation": "Companies Act (Chapter 49:03)",
        "weight": 25,
        "questions": [
            {
                "id": "mw-reg-1",
                "question": "Have you registered your company with the Registrar General's Office in Malawi?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "All companies operating in Malawi must be registered with the Registrar General.",
                "resource": "https://www.registrargeneral.gov.mw",
            },
            {
                "id": "mw-reg-2",
                "question": "Have you registered your business name with the Registrar General?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Trading names must be registered under the Business Names Registration Act.",
                "resource": "https://www.registrargeneral.gov.mw",
            },
            {
                "id": "mw-reg-3",
                "question": "Do you have a registered office address in Malawi?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "A registered office address in Malawi is required under the Companies Act.",
                "resource": "https://www.registrargeneral.gov.mw",
            },
            {
                "id": "mw-reg-4",
                "question": "Have you appointed local directors (at least one Malawi resident)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Companies Act requires at least one director resident in Malawi.",
                "resource": "https://www.registrargeneral.gov.mw",
            },
            {
                "id": "mw-reg-5",
                "question": "Have you obtained sector-specific licenses for your industry?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Certain industries require additional licensing (telecoms, banking, mining, etc.).",
            },
            {
                "id": "mw-reg-6",
                "question": "Have you filed your annual returns with the Registrar General?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Annual returns must be filed within 60 days of the company's anniversary.",
            },
        ],
    },
    "tax_compliance": {
        "name": "Tax Compliance",
        "regulation": "Income Tax Act (Chapter 44:06) & VAT Act (Chapter 4:05)",
        "weight": 25,
        "questions": [
            {
                "id": "mw-tax-1",
                "question": "Have you registered with the Malawi Revenue Authority (MRA)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "All businesses must register with MRA for tax purposes.",
                "resource": "https://www.mra.mw",
            },
            {
                "id": "mw-tax-2",
                "question": "Have you obtained a Taxpayer Identification Number (TPIN)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "A TPIN is required for all tax filings and business transactions.",
                "resource": "https://www.mra.mw",
            },
            {
                "id": "mw-tax-3",
                "question": "Are you registered for VAT (if turnover exceeds MK50 million)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "VAT registration is mandatory when annual turnover exceeds MK50 million.",
                "resource": "https://www.mra.mw",
            },
            {
                "id": "mw-tax-4",
                "question": "Do you remit PAYE for your employees?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "PAYE must be deducted and remitted to MRA monthly.",
            },
            {
                "id": "mw-tax-5",
                "question": "Do you file corporate income tax returns by the 30th of June?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Corporate tax returns due 30 June following end of fiscal year (31 Dec).",
                "resource": "https://www.mra.mw",
            },
            {
                "id": "mw-tax-6",
                "question": "Have you applied for a Tax Clearance Certificate (TCC)?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "TCC is often required for tenders, loans, and international transactions.",
            },
        ],
    },
    "employment_law": {
        "name": "Employment Law",
        "regulation": "Employment Act (Chapter 4:03)",
        "weight": 20,
        "questions": [
            {
                "id": "mw-emp-1",
                "question": "Do you use written employment contracts for all employees?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Employment contracts must be in writing under the Employment Act.",
            },
            {
                "id": "mw-emp-2",
                "question": "Do you comply with minimum wage requirements?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Malawi sets annual minimum wages for various sectors.",
            },
            {
                "id": "mw-emp-3",
                "question": "Do you register employees with the Malawi Social Security (NICO)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Employers must contribute to social security for employees.",
            },
            {
                "id": "mw-emp-4",
                "question": "Do you provide statutory annual leave (minimum 18 days)?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Employees entitled to at least 18 days annual leave per year.",
            },
            {
                "id": "mw-emp-5",
                "question": "Do you follow correct termination procedures?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Terminations must follow legal procedures including notice periods.",
            },
        ],
    },
    "immigration": {
        "name": "Work Permits & Immigration",
        "regulation": "Immigration Act (Chapter 15:08)",
        "weight": 15,
        "questions": [
            {
                "id": "mw-imm-1",
                "question": "Have you obtained work permits for foreign employees?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Foreign nationals need work permits to work in Malawi.",
                "resource": "https://www.immigration.gov.mw",
            },
            {
                "id": "mw-imm-2",
                "question": "Have you obtained business residence permits for business owners?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Foreign business owners need residence permits to operate in Malawi.",
                "resource": "https://www.immigration.gov.mw",
            },
            {
                "id": "mw-imm-3",
                "question": "Do you have an immigration quota for expatriate employees?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Malawi limits the number of expatriate workers per company.",
            },
        ],
    },
    "data_protection": {
        "name": "Data Protection",
        "regulation": "Data Protection Act (Chapter 4:10)",
        "weight": 15,
        "questions": [
            {
                "id": "mw-dpa-1",
                "question": "Have you registered with the Malawi Data Protection Authority?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Data controllers and processors must register with the authority.",
            },
            {
                "id": "mw-dpa-2",
                "question": "Do you have a privacy policy explaining how personal data is used?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Privacy policies are required under the Data Protection Act.",
            },
            {
                "id": "mw-dpa-3",
                "question": "Do you have procedures for data breach notification?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Data breaches must be reported within 72 hours.",
            },
            {
                "id": "mw-dpa-4",
                "question": "Do you obtain consent before collecting personal data?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Lawful basis and consent required for data processing.",
            },
        ],
    },
}

# ---------------------------------------------------------------------------
# ZAMBIA COMPLIANCE QUESTIONS
# Target: Malawians expanding into Zambia
# ---------------------------------------------------------------------------

ZAMBIA_QUESTIONS = {
    "business_registration": {
        "name": "Business Registration",
        "regulation": "Companies Act No. 10 of 2017",
        "weight": 25,
        "questions": [
            {
                "id": "zm-reg-1",
                "question": "Have you registered your company with the Patents and Companies Registration Agency (PACRA)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "All companies in Zambia must be registered with PACRA.",
                "resource": "https://www.pacra.org.zm",
            },
            {
                "id": "zm-reg-2",
                "question": "Have you registered your business name with PACRA?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Business names must be registered under the Registration of Business Names Act.",
                "resource": "https://www.pacra.org.zm",
            },
            {
                "id": "zm-reg-3",
                "question": "Do you have a registered office in Zambia?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "A registered office address in Zambia is required under the Companies Act.",
                "resource": "https://www.pacra.org.zm",
            },
            {
                "id": "zm-reg-4",
                "question": "Have you appointed at least two directors (one being a Zambian resident)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Zambia's Companies Act requires at least one director resident in Zambia.",
                "resource": "https://www.pacra.org.zm",
            },
            {
                "id": "zm-reg-5",
                "question": "Have you obtained sector-specific licenses (zambia agency, etc.)?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Some sectors require licenses (ZRA, ZEMA, ZICTA, banks).",
            },
            {
                "id": "zm-reg-6",
                "question": "Are you aware of the Citizens Economic Empowerment Act requirements?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "The CEE Act mandates local ownership participation in certain sectors.",
            },
        ],
    },
    "tax_compliance": {
        "name": "Tax Compliance",
        "regulation": "Income Tax Act No. 12 of 2015 & VAT Act No. 12 of 2018",
        "weight": 25,
        "questions": [
            {
                "id": "zm-tax-1",
                "question": "Have you registered with the Zambia Revenue Authority (ZRA)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "All businesses must register with ZRA.",
                "resource": "https://www.zra.org.zm",
            },
            {
                "id": "zm-tax-2",
                "question": "Have you obtained a Taxpayer Identification Number (TPIN)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "A TPIN is required for all business transactions in Zambia.",
                "resource": "https://www.zra.org.zm",
            },
            {
                "id": "zm-tax-3",
                "question": "Are you registered for VAT (if turnover exceeds ZMW 800,000)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "VAT registration is mandatory when annual turnover exceeds ZMW 800,000.",
                "resource": "https://www.zra.org.zm",
            },
            {
                "id": "zm-tax-4",
                "question": "Do you remit PAYE for your employees?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "PAYE must be deducted and remitted to ZRA.",
            },
            {
                "id": "zm-tax-5",
                "question": "Do you file corporate income tax returns by the 30th of June?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Corporate tax returns due 30 June following end of fiscal year (31 Dec).",
                "resource": "https://www.zra.org.zm",
            },
            {
                "id": "zm-tax-6",
                "question": "Have you applied for a Tax Clearance Certificate (TCC)?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "TCC is often required for tenders, loans, and international transactions.",
            },
        ],
    },
    "employment_law": {
        "name": "Employment Law",
        "regulation": "Employment Code Act No. 3 of 2019",
        "weight": 20,
        "questions": [
            {
                "id": "zm-emp-1",
                "question": "Do you use written employment contracts for all employees?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Written contracts are mandatory under the Employment Code Act.",
            },
            {
                "id": "zm-emp-2",
                "question": "Do you comply with minimum wage requirements?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Zambia sets minimum wages through statutory instruments.",
            },
            {
                "id": "zm-emp-3",
                "question": "Do you contribute to the National Pension Scheme Authority (NAPSA)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Employer and employee contributions to NAPSA are mandatory.",
                "resource": "https://www.napsa.org.zm",
            },
            {
                "id": "zm-emp-4",
                "question": "Do you provide statutory annual leave (minimum 24 days)?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Employees entitled to at least 24 days annual leave per year.",
            },
            {
                "id": "zm-emp-5",
                "question": "Do you follow correct termination and severance procedures?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Terminations must follow legal procedures including notice and severance.",
            },
        ],
    },
    "immigration": {
        "name": "Work Permits & Immigration",
        "regulation": "Immigration and Deportation Act",
        "weight": 15,
        "questions": [
            {
                "id": "zm-imm-1",
                "question": "Have you obtained work permits for foreign employees?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Foreign nationals need work permits to work in Zambia.",
                "resource": "https://www.zambiaimmigration.gov.zm",
            },
            {
                "id": "zm-imm-2",
                "question": "Have you obtained business residence permits for business owners?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Foreign business owners need residence permits to operate in Zambia.",
                "resource": "https://www.zambiaimmigration.gov.zm",
            },
            {
                "id": "zm-imm-3",
                "question": "Do you comply with the employment of expatriates ratio?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Foreign employees should be complemented by local employees.",
            },
        ],
    },
    "data_protection": {
        "name": "Data Protection",
        "regulation": "Data Protection Act No. 3 of 2021",
        "weight": 15,
        "questions": [
            {
                "id": "zm-dpa-1",
                "question": "Have you registered with the Zambia Data Protection Authority (ZDPA)?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Data controllers and processors must register with the ZDPA.",
            },
            {
                "id": "zm-dpa-2",
                "question": "Do you have a privacy policy explaining how personal data is used?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Privacy policies are required under the Data Protection Act.",
            },
            {
                "id": "zm-dpa-3",
                "question": "Do you have procedures for data breach notification?",
                "answer_type": "yes_no",
                "critical": False,
                "requirement": "Data breaches must be reported to the ZDPA.",
            },
            {
                "id": "zm-dpa-4",
                "question": "Do you obtain consent before collecting personal data?",
                "answer_type": "yes_no",
                "critical": True,
                "requirement": "Consent is required for collection of personal data.",
            },
        ],
    },
}

COUNTRIES = {
    "malawi": {
        "name": "Malawi",
        "flag": "🇲🇼",
        "currency": "Malawi Kwacha (MK)",
        "regulations": MALAWI_QUESTIONS,
    },
    "zambia": {
        "name": "Zambia",
        "flag": "🇿🇲",
        "currency": "Zambian Kwacha (ZMW)",
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