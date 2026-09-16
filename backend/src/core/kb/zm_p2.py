"""Journey phase from the ZM KB: phase 2 - Product & Trade Compliance."""

PHASE =         {
            "phase_number": 2,
            "name": "Product & Trade Compliance",
            "description": "Handle everything related to getting your product or service legally across the border — classifications, permits, certificates, and customs requirements.",
            "steps": [
                {
                    "slug": "obtain_certificate_of_origin",
                    "title": "Obtain Certificate of Origin",
                    "description": "Get a Certificate of Origin proving your products are manufactured or sourced in Zambia.",
                    "why_needed": "A Certificate of Origin is required to benefit from COMESA/SADC trade preferences (reduced tariffs) and is often required by Malawian customs. Without it, your goods face full import duty.",
                    "authority": "Zambia Chamber of Commerce and Industry (ZACCI)",
                    "documents_needed": [
                        "Application form from ZACCI",
                        "Commercial invoice",
                        "Packing list",
                        "Certificate of Incorporation",
                    ],
                    "instructions": (
                        "1. Apply to ZACCI for a Certificate of Origin\n"
                        "2. Submit your commercial invoice, packing list, and proof of company registration\n"
                        "3. ZACCI will verify and issue the certificate\n"
                        "4. The certificate is typically valid for a single shipment\n"
                        "5. For repeated exports, consider applying for a general Certificate of Origin"
                    ),
                    "estimated_cost": "ZMW 500 - 1,500 per certificate",
                    "estimated_timeline": "2-5 business days",
                    "official_source": "https://www.zacci.co.zm",
                    "depends_on": ["confirm_export_eligibility_zambia"],
                    "business_models": ["export", "distributor", "agent"],
                },
                {
                    "slug": "obtain_product_standards",
                    "title": "Obtain product standards certification",
                    "description": "Ensure your product meets Malawian standards and obtain the required certifications.",
                    "why_needed": "Malawi Bureau of Standards (MBS) requires certain products to meet Malawian or international standards before import. Non-compliant products will be rejected at the border.",
                    "authority": "Zambia Bureau of Standards (ZABS), Malawi Bureau of Standards (MBS)",
                    "documents_needed": [
                        "Product test reports (from accredited lab)",
                        "ZABS conformity certificate (for Zambia-manufactured goods)",
                        "MBS import permit (for regulated products)",
                    ],
                    "instructions": (
                        "1. Check MBS website for your product category requirements\n"
                        "2. Have your product tested at an accredited laboratory (ZABS in Zambia or MBS in Malawi)\n"
                        "3. Obtain ZABS conformity certificate if manufacturing in Zambia\n"
                        "4. Apply for MBS import permit if required for your product category\n"
                        "5. Ensure packaging and labelling meet Malawian requirements\n\n"
                        "Products commonly requiring certification:\n"
                        "- Food and beverages\n"
                        "- Electronics and electrical equipment\n"
                        "- Building materials\n"
                        "- Chemicals and cosmetics\n"
                        "- Toys and children's products"
                    ),
                    "estimated_cost": "USD 100 - 500 depending on product",
                    "estimated_timeline": "2-6 weeks",
                    "official_source": "https://www.mbs.mw",
                    "depends_on": ["confirm_product_classification"],
                    "business_models": ["export", "distributor"],
                },
                {
                    "slug": "obtain_export_permits",
                    "title": "Obtain any required export permits",
                    "description": "Check whether your specific product requires an export permit from a Zambian government agency.",
                    "why_needed": "Some products (agricultural produce, wildlife products, minerals) require specific export permits. Exporting without these can result in criminal penalties and seizure of goods.",
                    "authority": "varies — Ministry of Agriculture, Zambia Environmental Management Agency (ZEMA), CITES authority",
                    "documents_needed": [
                        "Export permit application",
                        "Product licence",
                        "Inspection certificate (for agricultural products)",
                    ],
                    "instructions": (
                        "1. Check if your product is on the controlled/export-restricted list\n"
                        "2. For agricultural products: Apply to the Ministry of Agriculture for export certification\n"
                        "3. For minerals: Obtain export permit from the Ministry of Mines\n"
                        "4. For wildlife products: Obtain CITES permit\n"
                        "5. For tobacco, tea, sugar: Get clearance from the respective marketing authorities"
                    ),
                    "estimated_cost": "Varies by product type",
                    "estimated_timeline": "1-4 weeks",
                    "official_source": None,
                    "depends_on": ["confirm_export_eligibility_zambia"],
                    "business_models": ["export", "distributor"],
                },
                {
                    "slug": "prepare_customs_documentation",
                    "title": "Prepare customs documentation",
                    "description": "Prepare all documents required for Malawian customs clearance.",
                    "why_needed": "Incomplete customs documentation is the #1 cause of border delays. Having everything ready before your shipment arrives saves time and money.",
                    "authority": "Malawi Revenue Authority (MRA) — Customs Division",
                    "documents_needed": [
                        "Commercial invoice",
                        "Packing list",
                        "Bill of Lading or Airway Bill",
                        "Certificate of Origin",
                        "Import permit (from MBS if applicable)",
                        "Export permit (from Zambia authorities if applicable)",
                        "Insurance certificate",
                        "Product conformity certificate",
                    ],
                    "instructions": (
                        "1. Prepare a detailed commercial invoice with:\n"
                        "   - Full description of goods\n"
                        "   - HS codes\n"
                        "   - Quantity and unit price\n"
                        "   - Total value\n"
                        "   - Country of origin\n"
                        "2. Prepare a packing list with weights and dimensions\n"
                        "3. Obtain a Bill of Lading (sea) or Airway Bill (air)\n"
                        "4. Ensure Certificate of Origin is attached\n"
                        "5. Attach all required permits and certificates\n"
                        "6. Consider using a licensed customs broker for clearance"
                    ),
                    "estimated_cost": "USD 50 - 200 for customs broker fees",
                    "estimated_timeline": "1-3 days (once goods arrive at border)",
                    "official_source": "https://www.mra.mw",
                    "depends_on": ["obtain_certificate_of_origin", "obtain_product_standards"],
                    "business_models": ["export", "distributor"],
                },
                {
                    "slug": "understand_tariffs_taxes",
                    "title": "Understand applicable tariffs and taxes",
                    "description": "Determine what import duties, VAT, and other taxes apply to your products when entering Malawi.",
                    "why_needed": "Knowing your costs upfront prevents unpleasant surprises at the border and helps you price your products correctly in the Malawian market.",
                    "authority": "Malawi Revenue Authority (MRA)",
                    "documents_needed": [],
                    "instructions": (
                        "1. Look up your HS code on the MRA tariff schedule\n"
                        "2. Determine the applicable import duty rate\n"
                        "3. Check if COMESA preferential rates apply (with Certificate of Origin)\n"
                        "4. Calculate 16.5% VAT on CIF value + duty\n"
                        "5. Check for any excise duty on your product category\n"
                        "6. Note: COMESA/SADC member states often get reduced or zero duty rates\n\n"
                        "Typical rates:\n"
                        "- Import duty: 0-25% (varies by product)\n"
                        "- VAT: 16.5% on CIF + duty\n"
                        "- Excise: varies (fuel, alcohol, tobacco, vehicles)"
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "1-2 days",
                    "official_source": "https://www.mra.mw",
                    "depends_on": ["confirm_product_classification"],
                    "business_models": ["export", "distributor"],
                },
            ],
        }
