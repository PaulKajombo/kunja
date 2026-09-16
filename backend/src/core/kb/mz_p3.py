"""Journey phase from the MZ KB: phase 3 - Target-Country Entry."""

PHASE =         {
            "phase_number": 3,
            "name": "Target-Country Entry",
            "description": "Establish your legal presence in Zambia. Requirements depend on your market-entry model — a distributor needs less than a local subsidiary.",
            "steps": [
                {
                    "slug": "determine_local_registration",
                    "title": "Determine if local registration is required",
                    "description": "Based on your business model, determine whether you need to register a company in Zambia.",
                    "why_needed": "Some business models require local registration, others do not. Exporting from Malawi may not require it, but operating a branch or subsidiary definitely does.",
                    "authority": "Patents and Companies Registration Agency (PACRA)",
                    "documents_needed": [],
                    "instructions": (
                        "**Export from Malawi (no local presence):**\n"
                        "→ Local registration is NOT required. You sell from Malawi.\n\n"
                        "**Distributor model:**\n"
                        "→ Local registration is NOT required for you. Your Zambian distributor handles local compliance.\n"
                        "→ However, you may want a local presence for tax efficiency.\n\n"
                        "**Agent model:**\n"
                        "→ Local registration is NOT required. Your agent operates under their own registration.\n\n"
                        "**Branch office:**\n"
                        "→ You MUST register a branch of your Malawian company with PACRA.\n\n"
                        "**Local subsidiary:**\n"
                        "→ You MUST register a new Zambian company with PACRA."
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "1-2 days (to determine requirement)",
                    "official_source": "https://www.pacra.org.zm",
                    "depends_on": ["define_market_entry_model"],
                    "business_models": None,
                },
                {
                    "slug": "register_company_pacra",
                    "title": "Register company with PACRA",
                    "description": "Register your branch office or local subsidiary with the Patents and Companies Registration Agency in Zambia.",
                    "why_needed": "PACRA registration is legally required before you can open bank accounts, sign leases, hire employees, or conduct any business in Zambia under a company name.",
                    "authority": "Patents and Companies Registration Agency (PACRA)",
                    "documents_needed": [
                        "Company name reservation confirmation",
                        "Memorandum of Association (for new subsidiary)",
                        "Board resolution (for branch office)",
                        "Certified copies of parent company Certificate of Incorporation (for branch)",
                        "Director identification documents (passports)",
                        "Proof of registered office address in Zambia",
                        "PACRA application forms",
                    ],
                    "instructions": (
                        "1. Reserve your company name at PACRA (online or in-person)\n"
                        "2. Prepare the Memorandum of Association (for subsidiary) or branch registration documents\n"
                        "3. Ensure at least one director is a Zambian resident (or obtain exemption)\n"
                        "4. Secure a registered office address in Zambia (can be your agent's or lawyer's office)\n"
                        "5. Submit application with all required documents\n"
                        "6. Pay registration fees\n"
                        "7. Collect Certificate of Incorporation (subsidiary) or Branch Registration Certificate"
                    ),
                    "estimated_cost": "USD 200 - 500 (registration fees)",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": "https://www.pacra.org.zm",
                    "depends_on": ["determine_local_registration"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "obtain_zambian_business_licence",
                    "title": "Obtain Zambian business licence",
                    "description": "Get a business licence from the local council or city authority where you will operate.",
                    "why_needed": "A business licence is required by law before commencing any commercial activity in Zambia. Operating without one can result in fines or closure.",
                    "authority": "Local Council / City Council",
                    "documents_needed": [
                        "Certificate of Incorporation or Branch Certificate",
                        "Tax Clearance Certificate from ZRA",
                        "Lease agreement or proof of premises",
                        "PACRA registration certificate",
                    ],
                    "instructions": (
                        "1. Contact the local council in the area where your office/premises will be located\n"
                        "2. Submit your PACRA registration certificate\n"
                        "3. Provide proof of premises (lease agreement)\n"
                        "4. Obtain a Tax Clearance Certificate from ZRA\n"
                        "5. Pay the annual business licence fee\n"
                        "6. Display the licence at your premises"
                    ),
                    "estimated_cost": "USD 100 - 500 per year",
                    "estimated_timeline": "1-2 weeks",
                    "official_source": None,
                    "depends_on": ["register_company_pacra"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "register_for_taxes_zambia",
                    "title": "Register for taxes in Zambia",
                    "description": "Register with the Zambia Revenue Authority for Income Tax and VAT.",
                    "why_needed": "You are legally required to register for tax before commencing business. Failure to register results in penalties and interest on any unpaid taxes.",
                    "authority": "Zambia Revenue Authority (ZRA)",
                    "documents_needed": [
                        "PACRA registration certificate",
                        "Director identification",
                        "Proof of business address",
                        "Bank account details",
                    ],
                    "instructions": (
                        "1. Register for Income Tax with ZRA (obtain TPIN)\n"
                        "2. Register for VAT if your annual turnover will exceed ZMW 800,000\n"
                        "3. Register for PAYE if you will have employees\n"
                        "4. Open a Zambian corporate bank account (required for tax payments)\n"
                        "5. Set up a system for filing returns (monthly VAT, annual income tax)"
                    ),
                    "estimated_cost": "Free (registration)",
                    "estimated_timeline": "1-2 weeks",
                    "official_source": "https://www.zra.org.zm",
                    "depends_on": ["register_company_pacra"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "obtain_sector_specific_permits",
                    "title": "Obtain sector-specific permits",
                    "description": "Apply for any industry-specific permits or licences required to operate your business in Zambia.",
                    "why_needed": "Many sectors require additional permits beyond basic company registration. Operating without sector permits can result in prosecution and business closure.",
                    "authority": "varies by industry",
                    "documents_needed": [
                        "Sector permit application",
                        "Company registration documents",
                        "Technical qualifications or certifications",
                    ],
                    "instructions": (
                        "Common sector permits in Zambia:\n\n"
                        "**Agriculture & Food:**\n"
                        "- Ministry of Agriculture permit\n"
                        "- Zambia Compulsory Standards Agency (ZCSA) certification\n"
                        "- Food and Drug Board clearance (for food products)\n\n"
                        "**Mining:**\n"
                        "- Ministry of Mines and Minerals Development licence\n"
                        "- Environmental Impact Assessment (EIA)\n\n"
                        "**Telecommunications:**\n"
                        "- Zambia Information and Communications Technology Authority (ZICTA) licence\n\n"
                        "**Financial Services:**\n"
                        "- Bank of Zambia licence\n\n"
                        "**Transport & Logistics:**\n"
                        "- Road Transport and Safety Agency (RTSA) permit\n"
                        "- Zambia National Shipping Line clearance"
                    ),
                    "estimated_cost": "Varies widely by industry",
                    "estimated_timeline": "2-12 weeks",
                    "official_source": None,
                    "depends_on": ["register_company_pacra", "register_for_taxes_zambia"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "set_up_banking",
                    "title": "Set up banking and payment arrangements",
                    "description": "Open a Zambian bank account and set up payment infrastructure for your operations.",
                    "why_needed": "A local bank account is essential for receiving payments, paying suppliers, paying employees, and meeting tax obligations in Zambia.",
                    "authority": "Commercial banks in Zambia",
                    "documents_needed": [
                        "Certificate of Incorporation or Branch Certificate",
                        "Board resolution authorising account opening",
                        "Director identification documents",
                        "Proof of business address",
                        "Tax Clearance Certificate",
                    ],
                    "instructions": (
                        "1. Choose a commercial bank in Zambia (Standard Bank, Stanbic, Absa, etc.)\n"
                        "2. Schedule a meeting with the business banking department\n"
                        "3. Submit all required documents\n"
                        "4. Open a business current account\n"
                        "5. Set up online/internet banking\n"
                        "6. Arrange foreign exchange facilities if needed for repatriating profits\n"
                        "7. Consider setting up mobile money integration (Airtel Money, MTN Mobile Money)"
                    ),
                    "estimated_cost": "USD 50 - 200 initial deposit",
                    "estimated_timeline": "1-2 weeks",
                    "official_source": None,
                    "depends_on": ["register_company_pacra", "register_for_taxes_zambia"],
                    "business_models": ["branch", "subsidiary"],
                },
            ],
        }
