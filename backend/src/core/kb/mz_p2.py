"""Journey phase from the MZ KB: phase 2 - Product & Trade Compliance."""

PHASE =         {
            "phase_number": 2,
            "name": "Product & Trade Compliance",
            "description": "Handle everything related to getting your product or service legally across the border — classifications, permits, certificates, and customs requirements.",
            "steps": [
                {
                    "slug": "obtain_certificate_of_origin",
                    "title": "Obtain Certificate of Origin",
                    "description": "Get a Certificate of Origin proving your products are manufactured or sourced in Malawi.",
                    "why_needed": "A Certificate of Origin is required to benefit from SADC trade preferences (reduced tariffs) and is often required by Zambian customs. Without it, your goods face full import duty.",
                    "authority": "Malawi Confederation of Chambers of Commerce and Industry (MCCCI)",
                    "documents_needed": [
                        "Application form from MCCCI",
                        "Commercial invoice",
                        "Packing list",
                        "Certificate of Incorporation",
                    ],
                    "instructions": (
                        "1. Apply to MCCCI (or your local Chamber of Commerce) for a Certificate of Origin\n"
                        "2. Submit your commercial invoice, packing list, and proof of company registration\n"
                        "3. MCCCI will verify and issue the certificate\n"
                        "4. The certificate is typically valid for a single shipment\n"
                        "5. For repeated exports, consider applying for a general Certificate of Origin"
                    ),
                    "estimated_cost": "MWK 5,000 - 15,000 per certificate",
                    "estimated_timeline": "2-5 business days",
                    "official_source": "https://www.mccci.org",
                    "depends_on": ["confirm_export_eligibility"],
                    "business_models": ["export", "distributor", "agent"],
                },
                {
                    "slug": "obtain_product_standards",
                    "title": "Obtain product standards certification",
                    "description": "Ensure your product meets Zambian standards and obtain the required certifications.",
                    "why_needed": "Zambia Bureau of Standards (ZABS) requires certain products to meet Zambian or international standards before import. Non-compliant products will be rejected at the border.",
                    "authority": "Zambia Bureau of Standards (ZABS), Malawi Bureau of Standards (MBS)",
                    "documents_needed": [
                        "Product test reports (from accredited lab)",
                        "MBS conformity certificate (for Malawi-manufactured goods)",
                        "ZABS import permit (for regulated products)",
                    ],
                    "instructions": (
                        "1. Check ZABS website for your product category requirements\n"
                        "2. Have your product tested at an accredited laboratory (MBS in Malawi or ZABS in Zambia)\n"
                        "3. Obtain MBS conformity certificate if manufacturing in Malawi\n"
                        "4. Apply for ZABS import permit if required for your product category\n"
                        "5. Ensure packaging and labelling meet Zambian requirements\n\n"
                        "Products commonly requiring certification:\n"
                        "- Food and beverages\n"
                        "- Electronics and electrical equipment\n"
                        "- Building materials\n"
                        "- Chemicals and cosmetics\n"
                        "- Toys and children's products"
                    ),
                    "estimated_cost": "USD 100 - 500 depending on product",
                    "estimated_timeline": "2-6 weeks",
                    "official_source": "https://www.zabs.org.zm",
                    "depends_on": ["confirm_product_classification"],
                    "business_models": ["export", "distributor"],
                },
                {
                    "slug": "obtain_export_permits",
                    "title": "Obtain any required export permits",
                    "description": "Check whether your specific product requires an export permit from a Malawi government agency.",
                    "why_needed": "Some products (agricultural produce, wildlife products, minerals) require specific export permits. Exporting without these can result in criminal penalties and seizure of goods.",
                    "authority": "varies — Department of Agriculture, Ministry of Mines, CITES authority",
                    "documents_needed": [
                        "Export permit application",
                        "Product licence",
                        "Inspection certificate (for agricultural products)",
                    ],
                    "instructions": (
                        "1. Check if your product is on the controlled/export-restricted list\n"
                        "2. For agricultural products: Apply to the Department of Agriculture for a phytosanitary certificate\n"
                        "3. For minerals: Obtain export permit from the Ministry of Mines\n"
                        "4. For wildlife products: Obtain CITES permit\n"
                        "5. For tobacco, tea, sugar: Get clearance from the respective marketing board"
                    ),
                    "estimated_cost": "Varies by product type",
                    "estimated_timeline": "1-4 weeks",
                    "official_source": None,
                    "depends_on": ["confirm_export_eligibility"],
                    "business_models": ["export", "distributor"],
                },
                {
                    "slug": "prepare_customs_documentation",
                    "title": "Prepare customs documentation",
                    "description": "Prepare all documents required for Zambian customs clearance.",
                    "why_needed": "Incomplete customs documentation is the #1 cause of border delays. Having everything ready before your shipment arrives saves time and money.",
                    "authority": "Zambia Revenue Authority (ZRA) — Customs Division",
                    "documents_needed": [
                        "Commercial invoice",
                        "Packing list",
                        "Bill of Lading or Airway Bill",
                        "Certificate of Origin",
                        "Import permit (from ZABS if applicable)",
                        "Export permit (from Malawi authorities if applicable)",
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
                    "estimated_cost": "USD 50-200 for customs broker fees",
                    "estimated_timeline": "1-3 days (once goods arrive at border)",
                    "official_source": "https://www.zra.org.zm",
                    "depends_on": ["obtain_certificate_of_origin", "obtain_product_standards"],
                    "business_models": ["export", "distributor"],
                },
                {
                    "slug": "understand_tariffs_taxes",
                    "title": "Understand applicable tariffs and taxes",
                    "description": "Determine what import duties, VAT, and other taxes apply to your products when entering Zambia.",
                    "why_needed": "Knowing your costs upfront prevents unpleasant surprises at the border and helps you price your products correctly in the Zambian market.",
                    "authority": "Zambia Revenue Authority (ZRA)",
                    "documents_needed": [],
                    "instructions": (
                        "1. Look up your HS code on the ZRA tariff schedule\n"
                        "2. Determine the applicable import duty rate\n"
                        "3. Check if SADC preferential rates apply (with Certificate of Origin)\n"
                        "4. Calculate 16% VAT on CIF value + duty\n"
                        "5. Check for any excise duty on your product category\n"
                        "6. Note: SADC member states often get reduced or zero duty rates\n\n"
                        "Typical rates:\n"
                        "- Import duty: 0-25% (varies by product)\n"
                        "- VAT: 16% on CIF + duty\n"
                        "- Excise: varies (fuel, alcohol, tobacco, vehicles)"
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "1-2 days",
                    "official_source": "https://www.zra.org.zm",
                    "depends_on": ["confirm_product_classification"],
                    "business_models": ["export", "distributor"],
                },
            ],
        }
