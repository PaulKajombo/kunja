"""Industry-specific journey modifiers and supported industries."""

INDUSTRY_MODIFIERS = INDUSTRY_MODIFIERS = {
    "malawi_zambia": {
        "agriculture": {
            "extra_steps": {
                2: [  # Phase 2 extras
                    {
                        "slug": "obtain_phytosanitary_certificate",
                        "title": "Obtain phytosanitary certificate",
                        "description": "Get a phytosanitary certificate from the Department of Agriculture for agricultural exports.",
                        "why_needed": "Zambia requires phytosanitary certificates for all plant and agricultural product imports to prevent the spread of pests and diseases.",
                        "authority": "Department of Agriculture — Malawi",
                        "documents_needed": [
                            "Phytosanitary certificate application",
                            "Product details (type, quantity, origin)",
                            "Inspection report",
                        ],
                        "instructions": (
                            "1. Contact the Department of Agriculture, Plant Protection Unit\n"
                            "2. Submit your export application with product details\n"
                            "3. Arrange for inspection of your products\n"
                            "4. Upon passing inspection, receive the phytosanitary certificate\n"
                            "5. Include the certificate with your customs documentation"
                        ),
                        "estimated_cost": "MWK 5,000 - 20,000",
                        "estimated_timeline": "3-7 business days",
                        "official_source": None,
                        "depends_on": ["confirm_export_eligibility"],
                        "business_models": ["export", "distributor"],
                    },
                ],
            },
        },
        "food_manufacturing": {
            "extra_steps": {
                2: [
                    {
                        "slug": "obtain_food_safety_certification",
                        "title": "Obtain food safety certification",
                        "description": "Get food safety certification from the Malawi Bureau of Standards and ensure compliance with Zambian food import regulations.",
                        "why_needed": "Food products are heavily regulated in both countries. Without proper food safety certification, your products cannot legally be imported into Zambia.",
                        "authority": "Malawi Bureau of Standards (MBS), Zambia Compulsory Standards Agency (ZCSA)",
                        "documents_needed": [
                            "MBS food safety certificate",
                            "HACCP certification (if applicable)",
                            "Product labelling approval",
                            "ZCSA import permit for food products",
                        ],
                        "instructions": (
                            "1. Apply for MBS food safety certification\n"
                            "2. Implement HACCP (Hazard Analysis Critical Control Points) if required\n"
                            "3. Ensure product labelling meets Zambian requirements (English language, nutritional info, expiry date)\n"
                            "4. Apply for ZCSA import permit\n"
                            "5. Arrange for product testing at an accredited laboratory"
                        ),
                        "estimated_cost": "USD 200 - 1,000",
                        "estimated_timeline": "4-8 weeks",
                        "official_source": "https://www.mbs.mw",
                        "depends_on": ["confirm_product_classification"],
                        "business_models": ["export", "distributor"],
                    },
                ],
            },
        },
        "technology": {
            "remove_steps": [
                "obtain_product_standards",  # software doesn't need ZABS
                "obtain_certificate_of_origin",  # not needed for digital services
                "prepare_customs_documentation",  # no physical goods
            ],
        },
        "mining": {
            "extra_steps": {
                2: [
                    {
                        "slug": "obtain_mining_export_permits",
                        "title": "Obtain mining sector export permits",
                        "description": "Secure mining-specific export permits from the Ministry of Mines.",
                        "why_needed": "Minerals and mining products are heavily regulated exports. Exporting without permits is a criminal offence.",
                        "authority": "Ministry of Mines and Minerals Development — Malawi",
                        "documents_needed": [
                            "Mining licence",
                            "Export permit application",
                            "Mineral assay certificate",
                        ],
                        "instructions": (
                            "1. Ensure you hold a valid mining licence from the Ministry of Mines\n"
                            "2. Apply for a mineral export permit\n"
                            "3. Provide assay certificates for the minerals being exported\n"
                            "4. Submit all documentation to the Ministry for approval"
                        ),
                        "estimated_cost": "Varies",
                        "estimated_timeline": "4-8 weeks",
                        "official_source": None,
                        "depends_on": ["confirm_export_eligibility"],
                        "business_models": ["export", "distributor"],
                    },
                ],
            },
        },
    },
    "zambia_malawi": {
        "agriculture": {
            "extra_steps": {
                2: [
                    {
                        "slug": "obtain_phytosanitary_certificate",
                        "title": "Obtain phytosanitary certificate",
                        "description": "Get a phytosanitary certificate for plant and agricultural exports to Malawi.",
                        "why_needed": "Malawi requires phytosanitary certificates for all plant and agricultural product imports to prevent the spread of pests and diseases.",
                        "authority": "Zambia Agricultural Research Institute (ZARI) — Plant Quarantine",
                        "documents_needed": [
                            "Phytosanitary certificate application",
                            "Product details (type, quantity, origin)",
                            "Inspection report",
                        ],
                        "instructions": (
                            "1. Contact the Plant Quarantine Unit of the Ministry of Agriculture in Zambia\n"
                            "2. Submit your export application with product details\n"
                            "3. Arrange for inspection of your products\n"
                            "4. Upon passing inspection, receive the phytosanitary certificate\n"
                            "5. Include the certificate with your customs documentation"
                        ),
                        "estimated_cost": "ZMW 500 - 2,000",
                        "estimated_timeline": "3-7 business days",
                        "official_source": None,
                        "depends_on": ["confirm_export_eligibility_zambia"],
                        "business_models": ["export", "distributor"],
                    },
                ],
            },
        },
        "food_manufacturing": {
            "extra_steps": {
                2: [
                    {
                        "slug": "obtain_food_safety_certification",
                        "title": "Obtain food safety certification",
                        "description": "Get food safety certification from the Zambia Bureau of Standards and ensure compliance with Malawi food import regulations.",
                        "why_needed": "Food products are heavily regulated in both countries. Without proper food safety certification, your products cannot legally be imported into Malawi.",
                        "authority": "Zambia Bureau of Standards (ZABS), Malawi Bureau of Standards (MBS)",
                        "documents_needed": [
                            "ZABS food safety certificate",
                            "HACCP certification (if applicable)",
                            "Product labelling approval",
                            "MBS import permit for food products",
                        ],
                        "instructions": (
                            "1. Apply for ZABS food safety certification\n"
                            "2. Implement HACCP (Hazard Analysis Critical Control Points) if required\n"
                            "3. Ensure product labelling meets Malawi requirements (English language, nutritional info, expiry date)\n"
                            "4. Apply for MBS import permit\n"
                            "5. Arrange for product testing at an accredited laboratory"
                        ),
                        "estimated_cost": "USD 200 - 1,000",
                        "estimated_timeline": "4-8 weeks",
                        "official_source": "https://www.zabs.org.zm",
                        "depends_on": ["confirm_product_classification"],
                        "business_models": ["export", "distributor"],
                    },
                ],
            },
        },
        "technology": {
            "remove_steps": [
                "obtain_product_standards",  # software doesn't need MBS
                "obtain_certificate_of_origin",  # not needed for digital services
                "prepare_customs_documentation",  # no physical goods
            ],
        },
        "mining": {
            "extra_steps": {
                2: [
                    {
                        "slug": "obtain_mining_export_permits",
                        "title": "Obtain mining sector export permits",
                        "description": "Secure mining-specific export permits from the Zambia Ministry of Mines.",
                        "why_needed": "Minerals and mining products are heavily regulated exports. Exporting without permits is a criminal offence.",
                        "authority": "Ministry of Mines and Minerals Development — Zambia",
                        "documents_needed": [
                            "Mining licence",
                            "Export permit application",
                            "Mineral assay certificate",
                        ],
                        "instructions": (
                            "1. Ensure you hold a valid mining licence from the Ministry of Mines\n"
                            "2. Apply for a mineral export permit\n"
                            "3. Provide assay certificates for the minerals being exported\n"
                            "4. Submit all documentation to the Ministry for approval"
                        ),
                        "estimated_cost": "Varies",
                        "estimated_timeline": "4-8 weeks",
                        "official_source": None,
                        "depends_on": ["confirm_export_eligibility_zambia"],
                        "business_models": ["export", "distributor"],
                    },
                ],
            },
        },
    },
}


SUPPORTED_INDUSTRIES = SUPPORTED_INDUSTRIES = [
    "general",
    "agriculture",
    "food_manufacturing",
    "technology",
    "mining",
    "retail",
    "manufacturing",
    "services",
    "transport",
    "finance",
]

