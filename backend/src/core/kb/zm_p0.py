"""Journey phase from the ZM KB: phase 0 - Pre-Planning."""

PHASE =         {
            "phase_number": 0,
            "name": "Pre-Planning",
            "description": "Before crossing the border, determine exactly what you want to do in Malawi and whether your product or service can enter the market.",
            "steps": [
                {
                    "slug": "define_market_entry_model",
                    "title": "Define your market-entry model",
                    "description": "Decide how you want to enter the Malawian market. This determines every step that follows.",
                    "why_needed": "Your market-entry model dictates which registrations, permits, and compliance obligations apply to you. A distributor has very different requirements than a local subsidiary.",
                    "authority": None,
                    "documents_needed": [],
                    "instructions": (
                        "Choose one of the following models:\n\n"
                        "**Export directly** — Sell Malawian customers from Zambia. No local presence needed.\n"
                        "**Distributor** — Partner with a Malawian company that resells your products.\n"
                        "**Agent** — Appoint a Malawian representative who sells on your behalf.\n"
                        "**Branch office** — Open a branch of your Zambian company in Malawi.\n"
                        "**Local subsidiary** — Register a new Malawian company."
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "1-2 weeks",
                    "official_source": None,
                    "depends_on": [],
                    "business_models": None,  # all models
                },
                {
                    "slug": "confirm_product_classification",
                    "title": "Confirm product/service classification",
                    "description": "Identify the HS code for your products or the service category for your offering.",
                    "why_needed": "Your product classification determines tariffs, permits, certifications, and whether your product is even allowed into Malawi. A food product faces very different rules than software.",
                    "authority": "Malawi Revenue Authority (MRA) — Customs Division",
                    "documents_needed": [
                        "Product specifications",
                        "Technical data sheets",
                        "Photographs of product and packaging",
                    ],
                    "instructions": (
                        "1. Look up your product on the MRA customs tariff schedule at mra.mw\n"
                        "2. Classify using the HS (Harmonized System) code — this is an international standard\n"
                        "3. Note any special conditions tied to your product code\n"
                        "4. For services, identify the relevant sector classification"
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "1-3 days",
                    "official_source": "https://www.mra.mw",
                    "depends_on": [],
                    "business_models": None,
                },
                {
                    "slug": "check_market_access",
                    "title": "Check market access and restrictions",
                    "description": "Verify whether your product or service is permitted for import into Malawi and identify any restrictions or bans.",
                    "why_needed": "Malawi restricts or bans certain imports (e.g., certain agricultural products, hazardous materials). Entering without checking can result in goods being seized at the border.",
                    "authority": "Malawi Investment and Trade Centre (MITC), MRA",
                    "documents_needed": [],
                    "instructions": (
                        "1. Check with the Malawi Investment and Trade Centre (MITC) for the list of restricted and prohibited imports\n"
                        "2. Check if your product falls under any sector-specific regulations\n"
                        "3. For agricultural products, check with the Ministry of Agriculture\n"
                        "4. For food products, check the Malawi Bureau of Standards (MBS)\n"
                        "5. For pharmaceuticals, check the Pharmacy, Medicines and Poisons Board\n"
                        "6. Note any import licences or permits required before shipping"
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "1-5 days",
                    "official_source": "https://www.mitc.mw",
                    "depends_on": ["confirm_product_classification"],
                    "business_models": None,
                },
            ],
        }
