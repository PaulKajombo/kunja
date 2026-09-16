"""Journey phase from the MZ KB: phase 1 - Home-Country Readiness."""

PHASE =         {
            "phase_number": 1,
            "name": "Home-Country Readiness",
            "description": "Before crossing the border, make sure your business is properly set up in Malawi. You cannot export or operate cross-border without these foundations.",
            "steps": [
                {
                    "slug": "confirm_company_registration_malawi",
                    "title": "Confirm company registration in Malawi",
                    "description": "Ensure your company is properly registered with the Registrar General's Office in Malawi.",
                    "why_needed": "A valid Certificate of Incorporation is required to open bank accounts, register for tax, sign contracts, and apply for export permits. Without it, you cannot legally do business.",
                    "authority": "Registrar General's Office — Malawi",
                    "documents_needed": [
                        "Certificate of Incorporation",
                        "Memorandum and Articles of Association",
                        "Company extract from the Registrar",
                    ],
                    "instructions": (
                        "1. If already registered: Obtain a certified copy of your Certificate of Incorporation\n"
                        "2. Obtain a company extract from the Registrar General showing current directors and shareholders\n"
                        "3. Verify your company is in good standing (annual returns filed)\n\n"
                        "If not yet registered:\n"
                        "1. Reserve your company name at the Registrar General's Office\n"
                        "2. Prepare the Memorandum and Articles of Association\n"
                        "3. Incorporate with at least two directors (one Malawi resident)\n"
                        "4. Pay the registration fee\n"
                        "5. Collect your Certificate of Incorporation"
                    ),
                    "estimated_cost": "MWK 50,000 - 200,000 (approx.)",
                    "estimated_timeline": "1-4 weeks",
                    "official_source": "https://www.registrargeneral.gov.mw",
                    "depends_on": [],
                    "business_models": ["export", "distributor", "agent", "branch", "subsidiary"],
                },
                {
                    "slug": "confirm_tax_registration_malawi",
                    "title": "Confirm tax registration in Malawi",
                    "description": "Ensure your company has a Taxpayer Identification Number (TPIN) and is registered with the Malawi Revenue Authority (MRA).",
                    "why_needed": "You need a valid TPIN to file tax returns, apply for tax clearance certificates, and meet export requirements. Without it, you cannot obtain the documents needed for cross-border trade.",
                    "authority": "Malawi Revenue Authority (MRA)",
                    "documents_needed": [
                        "Taxpayer Identification Number (TPIN) certificate",
                        "Tax Clearance Certificate (TCC)",
                    ],
                    "instructions": (
                        "1. Visit your nearest MRA service centre\n"
                        "2. Present your Certificate of Incorporation and company details\n"
                        "3. Register for Income Tax and VAT (if applicable)\n"
                        "4. Obtain your TPIN\n"
                        "5. Ensure all returns are up to date\n"
                        "6. Apply for a Tax Clearance Certificate — this is essential for export operations"
                    ),
                    "estimated_cost": "Free (registration), TCC processing time varies",
                    "estimated_timeline": "1-2 weeks",
                    "official_source": "https://www.mra.mw",
                    "depends_on": ["confirm_company_registration_malawi"],
                    "business_models": None,
                },
                {
                    "slug": "confirm_business_licence",
                    "title": "Confirm business licence and sector registration",
                    "description": "Obtain or verify any sector-specific business licences required in Malawi.",
                    "why_needed": "Different industries require different licences. An agricultural exporter needs a produce licence. A food manufacturer needs a food handling certificate. Operating without these licences is illegal.",
                    "authority": "varies by industry",
                    "documents_needed": [
                        "Business licence (from local council)",
                        "Sector-specific licence (varies)",
                    ],
                    "instructions": (
                        "1. Contact your local District Council for a general business licence\n"
                        "2. Check with the relevant industry body for sector-specific licences\n\n"
                        "Common sector licences in Malawi:\n"
                        "- Agriculture: Produce Marketing Board licence\n"
                        "- Food manufacturing: Food Safety certificate from MBS\n"
                        "- Mining: Ministry of Mining licence\n"
                        "- Telecoms: MACRA licence\n"
                        "- Financial services: Reserve Bank of Malawi licence\n"
                        "- Transport: Road Transport and Safety Agency (RTSA)"
                    ),
                    "estimated_cost": "Varies by industry",
                    "estimated_timeline": "1-4 weeks",
                    "official_source": None,
                    "depends_on": ["confirm_company_registration_malawi"],
                    "business_models": None,
                },
                {
                    "slug": "confirm_export_eligibility",
                    "title": "Confirm export eligibility and registration",
                    "description": "Register as an exporter with the relevant Malawi authorities and confirm your products are eligible for export.",
                    "why_needed": "Malawi has specific export requirements. Certain products (tobacco, tea, sugar) are regulated by marketing boards. You need export documentation to clear customs.",
                    "authority": "Malawi Revenue Authority (MRA) — Customs, Export Promotion Council",
                    "documents_needed": [
                        "Export licence (if applicable)",
                        "Export permit from relevant marketing board (for regulated products)",
                        "IEC (Importer Exporter Code) from MRA",
                    ],
                    "instructions": (
                        "1. Register for an Importer Exporter Code (IEC) with MRA Customs\n"
                        "2. For regulated agricultural products (tobacco, tea, sugar, coffee), obtain a licence from the relevant marketing board\n"
                        "3. Check if your product requires a phytosanitary certificate from the Department of Agriculture\n"
                        "4. Ensure your product meets Zambian import standards (ZABS)"
                    ),
                    "estimated_cost": "MWK 10,000 - 100,000 depending on product",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": "https://www.mra.mw",
                    "depends_on": ["confirm_company_registration_malawi", "confirm_tax_registration_malawi"],
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
                        "Power of Attorney (if using an agent in Zambia)",
                    ],
                    "instructions": (
                        "1. Make certified copies of your Certificate of Incorporation (at least 3 copies)\n"
                        "2. Get a Board Resolution authorising the company to operate in Zambia\n"
                        "3. Prepare a Power of Attorney if you are appointing a Zambian agent\n"
                        "4. Ensure all director passports are current\n"
                        "5. Have your Tax Clearance Certificate ready\n"
                        "6. Keep digital copies of everything in a secure folder"
                    ),
                    "estimated_cost": "MWK 10,000 - 30,000 for certified copies",
                    "estimated_timeline": "1 week",
                    "official_source": None,
                    "depends_on": ["confirm_company_registration_malawi", "confirm_tax_registration_malawi"],
                    "business_models": None,
                },
            ],
        }
