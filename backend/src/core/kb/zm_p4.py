"""Journey phase from the ZM KB: phase 4 - Operations Setup."""

PHASE =         {
            "phase_number": 4,
            "name": "Operations Setup",
            "description": "Set up the practical requirements to start operating — premises, people, logistics, and systems.",
            "steps": [
                {
                    "slug": "secure_premises",
                    "title": "Secure premises / registered office",
                    "description": "Find and secure office space, warehouse, or retail premises in Malawi.",
                    "why_needed": "You need a physical address for company registration, business licensing, and daily operations. The premises must be appropriate for your business type.",
                    "authority": None,
                    "documents_needed": [
                        "Lease agreement",
                        "Landlord's property title or consent",
                        "Council approval for business use",
                    ],
                    "instructions": (
                        "1. Identify suitable locations based on your business needs\n"
                        "2. Negotiate lease terms (typically 1-3 year leases)\n"
                        "3. Ensure the property is zoned for commercial use\n"
                        "4. Sign the lease agreement\n"
                        "5. Register the lease with the relevant authorities if required\n"
                        "6. Arrange utilities connection (ESCOM electricity, water boards)"
                    ),
                    "estimated_cost": "USD 300 - 3,000 per month (varies by location)",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": None,
                    "depends_on": ["register_company_rgo"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "arrange_work_permits",
                    "title": "Arrange work permits and employment",
                    "description": "If you or your employees will work in Malawi, obtain the required work and residence permits.",
                    "why_needed": "Foreign nationals cannot work in Malawi without a valid work permit. Working without one is a criminal offence that can result in deportation.",
                    "authority": "Department of Immigration and Citizenship Services (DICS) — Malawi",
                    "documents_needed": [
                        "Work permit application",
                        "Passport (valid for at least 6 months)",
                        "Employment contract",
                        "Company registration documents",
                        "Police clearance certificate",
                        "Medical certificate",
                        "Proof of qualifications",
                    ],
                    "instructions": (
                        "1. Determine the type of permit needed:\n"
                        "- **Business Residence Permit** — for business owners/investors\n"
                        "- **Temporary Employment Permit (TEP)** — for employed persons\n"
                        "- **Visitors Permit / Self-employment** — for short-term work\n"
                        "2. Gather all required documents\n"
                        "3. Submit application to the Department of Immigration and Citizenship Services\n"
                        "4. Pay the application fee\n"
                        "5. Wait for processing (can take 4-8 weeks)\n"
                        "6. Collect the permit\n\n"
                        "**Note:** For a distributor or agent model, you may not need work permits if you don't plan to live in Malawi."
                    ),
                    "estimated_cost": "USD 150 - 800 depending on permit type",
                    "estimated_timeline": "4-8 weeks",
                    "official_source": "https://www.immigration.gov.mw",
                    "depends_on": ["register_company_rgo"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "understand_employment_obligations",
                    "title": "Understand employment obligations",
                    "description": "Learn about your obligations as an employer under the Malawian Employment Act.",
                    "why_needed": "Malawi's Employment Act (Chapter 4:03) sets out minimum requirements for employment contracts, working hours, leave, termination, and worker safety. Non-compliance can result in penalties and labour disputes.",
                    "authority": "Ministry of Labour",
                    "documents_needed": [
                        "Employment contracts (for all employees)",
                        "Workplace safety certificate",
                        "Pension scheme registration",
                        "Workers compensation registration",
                    ],
                    "instructions": (
                        "1. Draft employment contracts compliant with the Employment Act\n"
                        "2. Register employees with a licensed pension provider (Pension Act 2011)\n"
                        "3. Register with the Workers Compensation Fund\n"
                        "4. Ensure workplace meets safety standards\n"
                        "5. Understand minimum wage requirements for your sector\n"
                        "6. Set up payroll for PAYE deductions"
                    ),
                    "estimated_cost": "Varies",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": "https://www.labour.gov.mw",
                    "depends_on": ["register_company_rgo"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "register_for_data_protection",
                    "title": "Register for data protection",
                    "description": "Register with the Malawi Data Protection Authority if you collect personal data.",
                    "why_needed": "The Malawi Data Protection Act requires all organisations that process personal data to register with the Data Protection Authority. Non-compliance carries significant fines.",
                    "authority": "Malawi Data Protection Authority",
                    "documents_needed": [
                        "Registration application",
                        "Privacy policy document",
                        "Data processing register",
                    ],
                    "instructions": (
                        "1. Draft a privacy policy for your Malawian operations\n"
                        "2. Create a data processing register (what data you collect, why, how)\n"
                        "3. Submit registration to the Data Protection Authority\n"
                        "4. Implement data security measures\n"
                        "5. Ensure you have consent mechanisms for data collection"
                    ),
                    "estimated_cost": "MWK 50,000 - 200,000",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": None,
                    "depends_on": ["register_company_rgo"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "set_up_logistics",
                    "title": "Set up logistics and supply chain",
                    "description": "Establish your logistics, warehousing, and distribution arrangements.",
                    "why_needed": "Efficient logistics are critical for cross-border trade. Choosing the wrong shipping route, customs broker, or warehouse can add weeks and thousands of dollars to your costs.",
                    "authority": None,
                    "documents_needed": [
                        "Freight forwarder contract",
                        "Warehouse lease agreement",
                        "Insurance policy",
                    ],
                    "instructions": (
                        "1. Choose your primary shipping route:\n"
                        "- **Road:** M1 highway via Mchinji border post (most common)\n"
                        "- **Rail:** SGR/CEAR rail link (for bulk goods)\n"
                        "- **Air:** Kenneth Kaunda International Airport → Kamuzu International Airport\n"
                        "2. Register with a licensed customs broker at the border\n"
                        "3. Secure warehouse space if needed\n"
                        "4. Arrange cargo insurance\n"
                        "5. Set up a tracking system for shipments\n"
                        "6. Consider using a freight forwarder for end-to-end logistics"
                    ),
                    "estimated_cost": "Varies",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": None,
                    "depends_on": [],
                    "business_models": ["export", "distributor"],
                },
            ],
        }
