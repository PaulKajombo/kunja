"""Journey phase from the ZM KB: phase 5 - Ongoing Compliance."""

PHASE =         {
            "phase_number": 5,
            "name": "Ongoing Compliance",
            "description": "Stay compliant with recurring obligations in both countries. Missing deadlines can result in penalties, fines, or loss of your business licence.",
            "steps": [
                {
                    "slug": "file_tax_returns_malawi",
                    "title": "File tax returns in Malawi",
                    "description": "Submit your corporate income tax returns and PAYE remittances on time.",
                    "why_needed": "Late filing results in penalties and interest. Persistent non-compliance can lead to prosecution and business closure.",
                    "authority": "Malawi Revenue Authority (MRA)",
                    "documents_needed": [
                        "Audited financial statements",
                        "Tax computation",
                        "VAT returns (monthly/quarterly)",
                        "PAYE returns (monthly)",
                    ],
                    "instructions": (
                        "Schedule:\n"
                        "- **VAT returns:** Monthly/quarterly, within the statutory deadline\n"
                        "- **PAYE:** Monthly, after payroll\n"
                        "- **Corporate income tax:** Annually, within 6 months of year-end\n"
                        "- **Provisional tax:** Quarterly payments based on estimated profits\n\n"
                        "1. Set up an accounting system from day one\n"
                        "2. Keep all invoices and receipts\n"
                        "3. Engage a local accountant or bookkeeper\n"
                        "4. File on time to avoid penalties"
                    ),
                    "estimated_cost": "Accountant fees: USD 100-500/month",
                    "estimated_timeline": "Ongoing (monthly/quarterly/annual)",
                    "official_source": "https://www.mra.mw",
                    "depends_on": ["register_for_taxes_malawi"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "file_annual_returns_rgo",
                    "title": "File annual returns with the Registrar General",
                    "description": "Submit your annual return to the Registrar General's Office to keep your company in good standing.",
                    "why_needed": "Failure to file annual returns results in your company being struck off the register. This means your company legally ceases to exist.",
                    "authority": "Registrar General's Office (RGO) — Malawi",
                    "documents_needed": [
                        "Annual return form",
                        "Audited financial statements (for large companies)",
                    ],
                    "instructions": (
                        "1. File your annual return within the statutory window after your company's anniversary\n"
                        "2. Submit the annual return form with updated company information\n"
                        "3. Include details of directors, shareholders, and registered office\n"
                        "4. Pay the filing fee\n"
                        "5. Keep a copy of the filed return"
                    ),
                    "estimated_cost": "USD 30 - 100",
                    "estimated_timeline": "Annually",
                    "official_source": "https://www.registrargeneral.gov.mw",
                    "depends_on": ["register_company_rgo"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "renew_business_licence",
                    "title": "Renew business licence annually",
                    "description": "Renew your local assembly business licence before it expires.",
                    "why_needed": "Operating with an expired business licence is illegal and can result in fines or closure of your business.",
                    "authority": "Local Assembly / City Council",
                    "documents_needed": [
                        "Renewal application",
                        "Tax Clearance Certificate",
                        "Previous year's licence",
                    ],
                    "instructions": (
                        "1. Note your licence renewal date (typically annually)\n"
                        "2. Obtain a fresh Tax Clearance Certificate from MRA\n"
                        "3. Submit renewal application to the local assembly\n"
                        "4. Pay the renewal fee\n"
                        "5. Collect and display the renewed licence"
                    ),
                    "estimated_cost": "USD 50 - 400 per year",
                    "estimated_timeline": "1-2 weeks before expiry",
                    "official_source": None,
                    "depends_on": ["obtain_malawi_business_licence"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "renew_work_permits",
                    "title": "Renew work permits before expiry",
                    "description": "Track and renew work permits and residence permits before they expire.",
                    "why_needed": "Working on an expired permit is a criminal offence. Renewal should be started at least 2 months before expiry.",
                    "authority": "Department of Immigration and Citizenship Services (DICS) — Malawi",
                    "documents_needed": [
                        "Permit renewal application",
                        "Current permit",
                        "Passport",
                        "Employment contract",
                        "Company registration documents",
                    ],
                    "instructions": (
                        "1. Mark permit expiry dates in your calendar\n"
                        "2. Begin renewal process at least 2 months before expiry\n"
                        "3. Gather updated documents\n"
                        "4. Submit renewal application\n"
                        "5. Pay the renewal fee\n"
                        "6. Do NOT let permits expire — this can result in deportation"
                    ),
                    "estimated_cost": "USD 150 - 600",
                    "estimated_timeline": "Start 2 months before expiry",
                    "official_source": "https://www.immigration.gov.mw",
                    "depends_on": ["arrange_work_permits"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "maintain_customs_compliance",
                    "title": "Maintain customs compliance",
                    "description": "Keep up with customs reporting obligations and maintain proper records for all cross-border shipments.",
                    "why_needed": "MRA conducts audits and inspections. Proper records protect you from penalties and help resolve any disputes quickly.",
                    "authority": "Malawi Revenue Authority (MRA) — Customs",
                    "documents_needed": [
                        "Import/export records",
                        "Customs declarations",
                        "Proof of payment of duties",
                    ],
                    "instructions": (
                        "1. Keep copies of all customs declarations\n"
                        "2. Maintain records of all duties paid\n"
                        "3. Keep shipping documents for at least 5 years\n"
                        "4. Respond promptly to any MRA audit requests\n"
                        "5. Consider an Authorized Economic Operator (AEO) status for faster clearance"
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "Ongoing",
                    "official_source": "https://www.mra.mw",
                    "depends_on": ["prepare_customs_documentation"],
                    "business_models": ["export", "distributor"],
                },
            ],
        }
