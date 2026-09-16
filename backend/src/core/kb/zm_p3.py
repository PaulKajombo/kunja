"""Journey phase from the ZM KB: phase 3 - Target-Country Entry."""

PHASE =         {
            "phase_number": 3,
            "name": "Target-Country Entry",
            "description": "Establish your legal presence in Malawi. Requirements depend on your market-entry model — a distributor needs less than a local subsidiary.",
            "steps": [
                {
                    "slug": "determine_local_registration",
                    "title": "Determine if local registration is required",
                    "description": "Based on your business model, determine whether you need to register a company in Malawi.",
                    "why_needed": "Some business models require local registration, others do not. Exporting from Zambia may not require it, but operating a branch or subsidiary definitely does.",
                    "authority": "Registrar General's Office (RGO) — Malawi",
                    "documents_needed": [],
                    "instructions": (
                        "**Export from Zambia (no local presence):**\n"
                        "→ Local registration is NOT required. You sell from Zambia.\n\n"
                        "**Distributor model:**\n"
                        "→ Local registration is NOT required for you. Your Malawian distributor handles local compliance.\n"
                        "→ However, you may want a local presence for tax efficiency.\n\n"
                        "**Agent model:**\n"
                        "→ Local registration is NOT required. Your agent operates under their own registration.\n\n"
                        "**Branch office:**\n"
                        "→ You MUST register a branch of your Zambian company with the Registrar General's Office.\n\n"
                        "**Local subsidiary:**\n"
                        "→ You MUST register a new Malawian company with the Registrar General's Office."
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "1-2 days (to determine requirement)",
                    "official_source": "https://www.registrargeneral.gov.mw",
                    "depends_on": ["define_market_entry_model"],
                    "business_models": None,
                },
                {
                    "slug": "register_company_rgo",
                    "title": "Register company with the Registrar General",
                    "description": "Register your branch office or local subsidiary with the Registrar General's Office in Malawi.",
                    "why_needed": "Company registration is legally required before you can open bank accounts, sign leases, hire employees, or conduct any business in Malawi under a company name.",
                    "authority": "Registrar General's Office (RGO) — Malawi",
                    "documents_needed": [
                        "Company name reservation confirmation",
                        "Memorandum and Articles of Association (for new subsidiary)",
                        "Board resolution (for branch office)",
                        "Certified copies of parent company Certificate of Incorporation (for branch)",
                        "Director identification documents (passports)",
                        "Proof of registered office address in Malawi",
                        "RGO application forms",
                    ],
                    "instructions": (
                        "1. Reserve your company name at the Registrar General's Office\n"
                        "2. Prepare the Memorandum and Articles of Association (for subsidiary) or branch registration documents\n"
                        "3. Ensure at least one director is a Malawi resident (or obtain exemption)\n"
                        "4. Secure a registered office address in Malawi (can be your agent's or lawyer's office)\n"
                        "5. Submit application with all required documents\n"
                        "6. Pay registration fees\n"
                        "7. Collect Certificate of Incorporation (subsidiary) or Branch Registration Certificate"
                    ),
                    "estimated_cost": "USD 100 - 300 (registration fees)",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": "https://www.registrargeneral.gov.mw",
                    "depends_on": ["determine_local_registration"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "obtain_malawi_business_licence",
                    "title": "Obtain business licence in Malawi",
                    "description": "Get a business licence from the local assembly or city council where you will operate.",
                    "why_needed": "A business licence is required by law before commencing any commercial activity in Malawi. Operating without one can result in fines or closure.",
                    "authority": "Local Assembly / City Council",
                    "documents_needed": [
                        "Certificate of Incorporation or Branch Certificate",
                        "Tax Clearance Certificate from MRA",
                        "Lease agreement or proof of premises",
                        "Registration certificate",
                    ],
                    "instructions": (
                        "1. Contact the local assembly in the area where your office/premises will be located\n"
                        "2. Submit your registration certificate\n"
                        "3. Provide proof of premises (lease agreement)\n"
                        "4. Obtain a Tax Clearance Certificate from MRA\n"
                        "5. Pay the annual business licence fee\n"
                        "6. Display the licence at your premises"
                    ),
                    "estimated_cost": "USD 50 - 400 per year",
                    "estimated_timeline": "1-2 weeks",
                    "official_source": None,
                    "depends_on": ["register_company_rgo"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "register_for_taxes_malawi",
                    "title": "Register for taxes in Malawi",
                    "description": "Register with the Malawi Revenue Authority for Income Tax and VAT.",
                    "why_needed": "You are legally required to register for tax before commencing business. Failure to register results in penalties and interest on any unpaid taxes.",
                    "authority": "Malawi Revenue Authority (MRA)",
                    "documents_needed": [
                        "Registration certificate",
                        "Director identification",
                        "Proof of business address",
                        "Bank account details",
                    ],
                    "instructions": (
                        "1. Register for Income Tax with MRA (obtain a TPIN)\n"
                        "2. Register for VAT if your annual turnover exceeds the registration threshold\n"
                        "3. Register for PAYE if you will have employees\n"
                        "4. Open a Malawian corporate bank account (required for tax payments)\n"
                        "5. Set up a system for filing returns (monthly VAT, annual income tax)"
                    ),
                    "estimated_cost": "Free (registration)",
                    "estimated_timeline": "1-2 weeks",
                    "official_source": "https://www.mra.mw",
                    "depends_on": ["register_company_rgo"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "obtain_malawi_sector_permits",
                    "title": "Obtain sector-specific permits",
                    "description": "Apply for any industry-specific permits or licences required to operate your business in Malawi.",
                    "why_needed": "Many sectors require additional permits beyond basic company registration. Operating without sector permits can result in prosecution and business closure.",
                    "authority": "varies by industry",
                    "documents_needed": [
                        "Sector permit application",
                        "Company registration documents",
                        "Technical qualifications or certifications",
                    ],
                    "instructions": (
                        "Common sector permits in Malawi:\n\n"
                        "**Agriculture & Food:**\n"
                        "- Ministry of Agriculture permits\n"
                        "- Malawi Bureau of Standards (MBS) certification\n"
                        "- Food and Drugs Board clearance (for food products)\n\n"
                        "**Mining:**\n"
                        "- Ministry of Mining permit\n"
                        "- Environmental Impact Assessment (EIA)\n\n"
                        "**Telecommunications:**\n"
                        "- Malawi Communications Regulatory Authority (MACRA) licence\n\n"
                        "**Financial Services:**\n"
                        "- Reserve Bank of Malawi licence\n\n"
                        "**Transport & Logistics:**\n"
                        "- Road Traffic Directorate permits\n"
                        "- Malawi Railways clearance for rail freight"
                    ),
                    "estimated_cost": "Varies widely by industry",
                    "estimated_timeline": "2-12 weeks",
                    "official_source": None,
                    "depends_on": ["register_company_rgo", "register_for_taxes_malawi"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "set_up_banking",
                    "title": "Set up banking and payment arrangements",
                    "description": "Open a Malawian bank account and set up payment infrastructure for your operations.",
                    "why_needed": "A local bank account is essential for receiving payments, paying suppliers, paying employees, and meeting tax obligations in Malawi.",
                    "authority": "Commercial banks in Malawi",
                    "documents_needed": [
                        "Certificate of Incorporation or Branch Certificate",
                        "Board resolution authorising account opening",
                        "Director identification documents",
                        "Proof of business address",
                        "Tax Clearance Certificate",
                    ],
                    "instructions": (
                        "1. Choose a commercial bank in Malawi (National Bank, Standard Bank, FDH, First Capital)\n"
                        "2. Schedule a meeting with the business banking department\n"
                        "3. Submit all required documents\n"
                        "4. Open a business current account\n"
                        "5. Set up online/internet banking\n"
                        "6. Arrange foreign exchange facilities if needed for repatriating profits\n"
                        "7. Consider setting up mobile money integration (Airtel Money, TNM Mpamba)"
                    ),
                    "estimated_cost": "USD 50 - 200 initial deposit",
                    "estimated_timeline": "1-2 weeks",
                    "official_source": None,
                    "depends_on": ["register_company_rgo", "register_for_taxes_malawi"],
                    "business_models": ["branch", "subsidiary"],
                },
            ],
        }
