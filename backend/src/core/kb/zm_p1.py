"""Journey phase from the ZM KB: phase 1 - Home-Country Readiness."""

PHASE =         {
            "phase_number": 1,
            "name": "Home-Country Readiness",
            "description": "Before crossing the border, make sure your business is properly set up in Zambia. You cannot export or operate cross-border without these foundations.",
            "steps": [
                {
                    "slug": "confirm_company_registration_zambia",
                    "title": "Confirm company registration in Zambia",
                    "description": "Ensure your company is properly registered with the Patents and Companies Registration Agency in Zambia.",
                    "why_needed": "A valid Certificate of Incorporation is required to open bank accounts, register for tax, sign contracts, and apply for export permits. Without it, you cannot legally do business.",
                    "authority": "Patents and Companies Registration Agency (PACRA)",
                    "documents_needed": [
                        "Certificate of Incorporation",
                        "Memorandum and Articles of Association",
                        "Company extract from PACRA",
                    ],
                    "instructions": (
                        "1. If already registered: Obtain a certified copy of your Certificate of Incorporation\n"
                        "2. Obtain a company extract from PACRA showing current directors and shareholders\n"
                        "3. Verify your company is in good standing (annual returns filed)\n\n"
                        "If not yet registered:\n"
                        "1. Reserve your company name at PACRA\n"
                        "2. Prepare the Memorandum and Articles of Association\n"
                        "3. Incorporate with at least one Zambian resident director\n"
                        "4. Pay the registration fee\n"
                        "5. Collect your Certificate of Incorporation"
                    ),
                    "estimated_cost": "ZMW 1,500 - 5,000 (approx.)",
                    "estimated_timeline": "1-4 weeks",
                    "official_source": "https://www.pacra.org.zm",
                    "depends_on": [],
                    "business_models": ["export", "distributor", "agent", "branch", "subsidiary"],
                },
                {
                    "slug": "confirm_tax_registration_zambia",
                    "title": "Confirm tax registration in Zambia",
                    "description": "Ensure your company has a Taxpayer Identification Number (TPIN) and is registered with the Zambia Revenue Authority (ZRA).",
                    "why_needed": "You need a valid TPIN to file tax returns, apply for tax clearance certificates, and meet export requirements. Without it, you cannot obtain the documents needed for cross-border trade.",
                    "authority": "Zambia Revenue Authority (ZRA)",
                    "documents_needed": [
                        "Taxpayer Identification Number (TPIN)",
                        "Tax Clearance Certificate (TCC)",
                    ],
                    "instructions": (
                        "1. Visit your nearest ZRA service centre or register online\n"
                        "2. Present your Certificate of Incorporation and company details\n"
                        "3. Register for Income Tax and VAT (if applicable)\n"
                        "4. Obtain your TPIN\n"
                        "5. Ensure all returns are up to date\n"
                        "6. Apply for a Tax Clearance Certificate — this is essential for export operations"
                    ),
                    "estimated_cost": "Free (registration), TCC processing time varies",
                    "estimated_timeline": "1-2 weeks",
                    "official_source": "https://www.zra.org.zm",
                    "depends_on": ["confirm_company_registration_zambia"],
                    "business_models": None,
                },
                {
                    "slug": "confirm_business_licence",
                    "title": "Confirm business licence and sector registration",
                    "description": "Obtain or verify any sector-specific business licences required in Zambia.",
                    "why_needed": "Different industries require different licences. A food manufacturer needs food handling certification. Operating without these licences is illegal.",
                    "authority": "Local Council / City Council",
                    "documents_needed": [
                        "Business licence (from local council)",
                        "Sector-specific licence (varies)",
                    ],
                    "instructions": (
                        "1. Contact your local council for a general business licence\n"
                        "2. Check with the relevant industry body for sector-specific licences\n\n"
                        "Common sector licences in Zambia:\n"
                        "- Food manufacturing: Zambia Compulsory Standards Agency (ZCSA)\n"
                        "- Mining: Ministry of Mines licence\n"
                        "- Telecoms: ZICTA licence\n"
                        "- Financial services: Bank of Zambia licence\n"
                        "- Transport: Road Transport and Safety Agency (RTSA)"
                    ),
                    "estimated_cost": "Varies by industry",
                    "estimated_timeline": "1-4 weeks",
                    "official_source": None,
                    "depends_on": ["confirm_company_registration_zambia"],
                    "business_models": None,
                },
                {
                    "slug": "confirm_export_eligibility_zambia",
                    "title": "Confirm export eligibility and registration",
                    "description": "Register as an exporter with the relevant Zambia authorities and confirm your products are eligible for export.",
                    "why_needed": "Zambia has specific export requirements. Certain products are regulated by sector authorities. You need export documentation to clear customs.",
                    "authority": "Zambia Revenue Authority (ZRA) — Customs, Zambia Bureau of Standards (ZABS)",
                    "documents_needed": [
                        "Export licence (if applicable)",
                        "ZABS export conformity certificate (for regulated products)",
                        "Importer Exporter Code (IEC) from ZRA",
                    ],
                    "instructions": (
                        "1. Register for an Importer Exporter Code (IEC) with ZRA Customs\n"
                        "2. For regulated agricultural products, obtain export certification from the relevant authority\n"
                        "3. Check if your product requires a phytosanitary certificate from the Ministry of Agriculture\n"
                        "4. Ensure your product meets Malawian import standards (MBS)"
                    ),
                    "estimated_cost": "ZMW 500 - 10,000 depending on product",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": "https://www.zra.org.zm",
                    "depends_on": ["confirm_company_registration_zambia", "confirm_tax_registration_zambia"],
                    "business_models": ["export", "distributor", "agent"],
                },
                {
                    "slug": "prepare_business_documents",
                    "title": "Prepare required business documents",
                    "description": "Gather and prepare all the documents you will need for cross-border operations.",
                    "why_needed": "Having documents ready before you need them prevents delays at borders, in banks, and during registration processes.",
                    "authority": None,
                    "documents_needed": [
                        "Certified copies of Certificate of Incorporation",
                        "Certified copies of Memorandum and Articles of Association",
                        "Tax Clearance Certificate",
                        "Board resolution authorising cross-border operations",
                        "Proof of registered office address",
                        "Director identification documents (passports)",
                        "Power of Attorney (if using an agent in Malawi)",
                    ],
                    "instructions": (
                        "1. Make certified copies of your Certificate of Incorporation (at least 3 copies)\n"
                        "2. Get a Board Resolution authorising the company to operate in Malawi\n"
                        "3. Prepare a Power of Attorney if you are appointing a Malawian agent\n"
                        "4. Ensure all director passports are current\n"
                        "5. Have your Tax Clearance Certificate ready\n"
                        "6. Keep digital copies of everything in a secure folder"
                    ),
                    "estimated_cost": "ZMW 500 - 3,000 for certified copies",
                    "estimated_timeline": "1 week",
                    "official_source": None,
                    "depends_on": ["confirm_company_registration_zambia", "confirm_tax_registration_zambia"],
                    "business_models": None,
                },
            ],
        }
