"""
Journey Knowledge Base for Kunja.

Defines the complete market-entry journey for each country pair,
including phases, steps, dependencies, and industry/business-model modifiers.

Architecture:
    CountryPair → Phases → Steps → (filtered by industry + business model)

Each step answers 7 questions:
    1. What is this? (description)
    2. Why do I need it? (why_needed)
    3. Who is responsible? (authority)
    4. What do I need? (documents_needed)
    5. How do I do it? (instructions)
    6. How much does it cost? (estimated_cost)
    7. How long does it take? (estimated_timeline)
"""

# ─────────────────────────────────────────────
# Malawi → Zambia Journey
# ─────────────────────────────────────────────

MALAWI_ZAMBIA_JOURNEY = {
    "origin": "malawi",
    "target": "zambia",
    "origin_name": "Malawi",
    "target_name": "Zambia",
    "origin_flag": "🇲🇼",
    "target_flag": "🇿🇲",
    "phases": [
        # ── Phase 0: Pre-Planning ──
        {
            "phase_number": 0,
            "name": "Pre-Planning",
            "description": "Before crossing the border, determine exactly what you want to do in Zambia and whether your product or service can enter the market.",
            "steps": [
                {
                    "slug": "define_market_entry_model",
                    "title": "Define your market-entry model",
                    "description": "Decide how you want to enter the Zambian market. This determines every step that follows.",
                    "why_needed": "Your market-entry model dictates which registrations, permits, and compliance obligations apply to you. A distributor has very different requirements than a local subsidiary.",
                    "authority": None,
                    "documents_needed": [],
                    "instructions": (
                        "Choose one of the following models:\n\n"
                        "**Export directly** — Sell Zambian customers from Malawi. No local presence needed.\n"
                        "**Distributor** — Partner with a Zambian company that resells your products.\n"
                        "**Agent** — Appoint a Zambian representative who sells on your behalf.\n"
                        "**Branch office** — Open a branch of your Malawian company in Zambia.\n"
                        "**Local subsidiary** — Register a new Zambian company."
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
                    "why_needed": "Your product classification determines tariffs, permits, certifications, and whether your product is even allowed into Zambia. A food product faces very different rules than software.",
                    "authority": "Zambia Revenue Authority (ZRA) — Customs Division",
                    "documents_needed": [
                        "Product specifications",
                        "Technical data sheets",
                        "Photographs of product and packaging",
                    ],
                    "instructions": (
                        "1. Look up your product on the ZRA customs tariff schedule at zra.org.zm\n"
                        "2. Classify using the HS (Harmonized System) code — this is an international standard\n"
                        "3. Note any special conditions tied to your product code\n"
                        "4. For services, identify the relevant sector classification"
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "1-3 days",
                    "official_source": "https://www.zra.org.zm",
                    "depends_on": [],
                    "business_models": None,
                },
                {
                    "slug": "check_market_access",
                    "title": "Check market access and restrictions",
                    "description": "Verify whether your product or service is permitted for import into Zambia and identify any restrictions or bans.",
                    "why_needed": "Zambia restricts or bans certain imports (e.g., used clothing, certain agricultural products, hazardous materials). Entering without checking can result in goods being seized at the border.",
                    "authority": "Zambia Development Agency (ZDA), ZRA",
                    "documents_needed": [],
                    "instructions": (
                        "1. Check the ZDA website for the list of restricted and prohibited imports\n"
                        "2. Check if your product falls under any sector-specific regulations\n"
                        "3. For agricultural products, check with the Ministry of Agriculture\n"
                        "4. For food products, check Zambia Bureau of Standards (ZABS)\n"
                        "5. For pharmaceuticals, check the Pharmaceutical Regulatory Authority\n"
                        "6. Note any import licences or permits required before shipping"
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "1-5 days",
                    "official_source": "https://www.zda.org.zm",
                    "depends_on": ["confirm_product_classification"],
                    "business_models": None,
                },
            ],
        },
        # ── Phase 1: Home-Country Readiness ──
        {
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
        },
        # ── Phase 2: Product & Trade Compliance ──
        {
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
        },
        # ── Phase 3: Target-Country Entry ──
        {
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
        },
        # ── Phase 4: Operations Setup ──
        {
            "phase_number": 4,
            "name": "Operations Setup",
            "description": "Set up the practical requirements to start operating — premises, people, logistics, and systems.",
            "steps": [
                {
                    "slug": "secure_premises",
                    "title": "Secure premises / registered office",
                    "description": "Find and secure office space, warehouse, or retail premises in Zambia.",
                    "why_needed": "You need a physical address for PACRA registration, business licensing, and daily operations. The premises must be appropriate for your business type.",
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
                        "6. Arrange utilities connection (ZESCO electricity, ZNWC water)"
                    ),
                    "estimated_cost": "USD 500 - 5,000 per month (varies by location)",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": None,
                    "depends_on": ["register_company_pacra"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "arrange_work_permits",
                    "title": "Arrange work permits and employment",
                    "description": "If you or your employees will work in Zambia, obtain the required work and residence permits.",
                    "why_needed": "Foreign nationals cannot work in Zambia without a valid work permit. Working without one is a criminal offence that can result in deportation.",
                    "authority": "Department of Immigration — Zambia",
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
                        "- **Investor's Permit** — for business owners/investors\n"
                        "- **Class B Work Permit** — for employed persons\n"
                        "- **Class G Permit** — for self-employed\n"
                        "2. Gather all required documents\n"
                        "3. Submit application to the Department of Immigration\n"
                        "4. Pay the application fee\n"
                        "5. Wait for processing (can take 4-8 weeks)\n"
                        "6. Collect the permit\n\n"
                        "**Note:** For a distributor or agent model, you may not need work permits if you don't plan to live in Zambia."
                    ),
                    "estimated_cost": "USD 200 - 1,000 depending on permit type",
                    "estimated_timeline": "4-8 weeks",
                    "official_source": "https://www.immigration.gov.zm",
                    "depends_on": ["register_company_pacra"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "understand_employment_obligations",
                    "title": "Understand employment obligations",
                    "description": "Learn about your obligations as an employer under the Zambian Employment Code Act.",
                    "why_needed": "Zambia's Employment Code Act No. 3 of 2019 sets out minimum requirements for employment contracts, working hours, leave, termination, and worker safety. Non-compliance can result in penalties and labour disputes.",
                    "authority": "Ministry of Labour and Social Security",
                    "documents_needed": [
                        "Employment contracts (for all employees)",
                        "Workplace safety certificate",
                        "NAPSA registration",
                        "Workers Compensation Fund registration",
                    ],
                    "instructions": (
                        "1. Draft employment contracts compliant with the Employment Code Act\n"
                        "2. Register with NAPSA (National Pension Scheme Authority) for employee pensions\n"
                        "3. Register with the Workers Compensation Fund\n"
                        "4. Ensure workplace meets safety standards\n"
                        "5. Understand minimum wage requirements for your sector\n"
                        "6. Set up payroll for PAYE deductions"
                    ),
                    "estimated_cost": "Varies",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": "https://www.molss.gov.zm",
                    "depends_on": ["register_company_pacra"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "register_for_data_protection",
                    "title": "Register for data protection",
                    "description": "Register with the Zambia Data Protection Authority if you collect personal data.",
                    "why_needed": "The Data Protection Act No. 3 of 2021 requires all organisations that process personal data to register with the Data Protection Authority. Non-compliance carries significant fines.",
                    "authority": "Zambia Data Protection Authority",
                    "documents_needed": [
                        "Registration application",
                        "Privacy policy document",
                        "Data processing register",
                    ],
                    "instructions": (
                        "1. Draft a privacy policy for your Zambian operations\n"
                        "2. Create a data processing register (what data you collect, why, how)\n"
                        "3. Submit registration to the Data Protection Authority\n"
                        "4. Implement data security measures\n"
                        "5. Ensure you have consent mechanisms for data collection"
                    ),
                    "estimated_cost": "ZMW 5,000 - 20,000",
                    "estimated_timeline": "2-4 weeks",
                    "official_source": "https://www.datagov.zm",
                    "depends_on": ["register_company_pacra"],
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
                        "- **Rail:** CeFDAR rail link (for bulk goods)\n"
                        "- **Air:** Kamuzu International Airport → Kenneth Kaunda International Airport\n"
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
        },
        # ── Phase 5: Ongoing Compliance ──
        {
            "phase_number": 5,
            "name": "Ongoing Compliance",
            "description": "Stay compliant with recurring obligations in both countries. Missing deadlines can result in penalties, fines, or loss of your business licence.",
            "steps": [
                {
                    "slug": "file_tax_returns_zambia",
                    "title": "File tax returns in Zambia",
                    "description": "Submit your corporate income tax returns and PAYE remittances on time.",
                    "why_needed": "Late filing results in penalties and interest. Persistent non-compliance can lead to prosecution and business closure.",
                    "authority": "Zambia Revenue Authority (ZRA)",
                    "documents_needed": [
                        "Audited financial statements",
                        "Tax computation",
                        "VAT returns (monthly/quarterly)",
                        "PAYE returns (monthly)",
                    ],
                    "instructions": (
                        "Schedule:\n"
                        "- **VAT returns:** Monthly, by the 18th of the following month\n"
                        "- **PAYE:** Monthly, by the 10th of the following month\n"
                        "- **Corporate income tax:** Annually, within 6 months of year-end\n"
                        "- **Provisional tax:** Quarterly payments based on estimated profits\n\n"
                        "1. Set up an accounting system from day one\n"
                        "2. Keep all invoices and receipts\n"
                        "3. Engage a local accountant or bookkeeper\n"
                        "4. File on time to avoid penalties"
                    ),
                    "estimated_cost": "Accountant fees: USD 100-500/month",
                    "estimated_timeline": "Ongoing (monthly/quarterly/annual)",
                    "official_source": "https://www.zra.org.zm",
                    "depends_on": ["register_for_taxes_zambia"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "file_annual_returns_pacra",
                    "title": "File annual returns with PACRA",
                    "description": "Submit your annual return to PACRA to keep your company in good standing.",
                    "why_needed": "Failure to file annual returns results in your company being struck off the register. This means your company legally ceases to exist.",
                    "authority": "Patents and Companies Registration Agency (PACRA)",
                    "documents_needed": [
                        "Annual return form",
                        "Audited financial statements (for large companies)",
                    ],
                    "instructions": (
                        "1. File annual return within 6 months of your company's anniversary\n"
                        "2. Submit the annual return form with updated company information\n"
                        "3. Include details of directors, shareholders, and registered office\n"
                        "4. Pay the filing fee\n"
                        "5. Keep a copy of the filed return"
                    ),
                    "estimated_cost": "USD 50 - 150",
                    "estimated_timeline": "Annually",
                    "official_source": "https://www.pacra.org.zm",
                    "depends_on": ["register_company_pacra"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "renew_business_licence",
                    "title": "Renew business licence annually",
                    "description": "Renew your local council business licence before it expires.",
                    "why_needed": "Operating with an expired business licence is illegal and can result in fines or closure of your business.",
                    "authority": "Local Council / City Council",
                    "documents_needed": [
                        "Renewal application",
                        "Tax Clearance Certificate",
                        "Previous year's licence",
                    ],
                    "instructions": (
                        "1. Note your licence renewal date (typically annually)\n"
                        "2. Obtain a fresh Tax Clearance Certificate from ZRA\n"
                        "3. Submit renewal application to the local council\n"
                        "4. Pay the renewal fee\n"
                        "5. Collect and display the renewed licence"
                    ),
                    "estimated_cost": "USD 100 - 500 per year",
                    "estimated_timeline": "1-2 weeks before expiry",
                    "official_source": None,
                    "depends_on": ["obtain_zambian_business_licence"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "renew_work_permits",
                    "title": "Renew work permits before expiry",
                    "description": "Track and renew work permits and residence permits before they expire.",
                    "why_needed": "Working on an expired permit is a criminal offence. Renewal should be started at least 2 months before expiry.",
                    "authority": "Department of Immigration — Zambia",
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
                    "estimated_cost": "USD 200 - 800",
                    "estimated_timeline": "Start 2 months before expiry",
                    "official_source": "https://www.immigration.gov.zm",
                    "depends_on": ["arrange_work_permits"],
                    "business_models": ["branch", "subsidiary"],
                },
                {
                    "slug": "maintain_customs_compliance",
                    "title": "Maintain customs compliance",
                    "description": "Keep up with customs reporting obligations and maintain proper records for all cross-border shipments.",
                    "why_needed": "ZRA conducts audits and inspections. Proper records protect you from penalties and help resolve any disputes quickly.",
                    "authority": "Zambia Revenue Authority (ZRA) — Customs",
                    "documents_needed": [
                        "Import/export records",
                        "Customs declarations",
                        "Proof of payment of duties",
                    ],
                    "instructions": (
                        "1. Keep copies of all customs declarations (SAD forms)\n"
                        "2. Maintain records of all duties paid\n"
                        "3. Keep shipping documents for at least 5 years\n"
                        "4. Respond promptly to any ZRA audit requests\n"
                        "5. Consider an Authorized Economic Operator (AEO) status for faster clearance"
                    ),
                    "estimated_cost": None,
                    "estimated_timeline": "Ongoing",
                    "official_source": "https://www.zra.org.zm",
                    "depends_on": ["prepare_customs_documentation"],
                    "business_models": ["export", "distributor"],
                },
            ],
        },
    ],
}


# ─────────────────────────────────────────────
# Zambia → Malawi Journey
# ─────────────────────────────────────────────

ZAMBIA_MALAWI_JOURNEY = {
    "origin": "zambia",
    "target": "malawi",
    "origin_name": "Zambia",
    "target_name": "Malawi",
    "origin_flag": "🇿🇲",
    "target_flag": "🇲🇼",
    "phases": [
        # ── Phase 0: Pre-Planning ──
        {
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
        },
        # ── Phase 1: Home-Country Readiness ──
        {
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
        },
        # ── Phase 2: Product & Trade Compliance ──
        {
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
        },
        # ── Phase 3: Target-Country Entry ──
        {
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
        },
        # ── Phase 4: Operations Setup ──
        {
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
        },
        # ── Phase 5: Ongoing Compliance ──
        {
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
        },
    ],
}


# ─────────────────────────────────────────────
# Industry Modifiers
# ─────────────────────────────────────────────
# Steps to add/modify/remove based on the user's industry.
# Modifiers are keyed by country pair ("origin_target") so the same
# industry can behave differently in each direction.

INDUSTRY_MODIFIERS = {
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

# ─────────────────────────────────────────────
# Business Model Info
# ─────────────────────────────────────────────
# Display info for each market-entry model. Steps are filtered by the
# `business_models` field on each KB step, so no per-model remove list is
# needed — the same journey shape works for both country pairs.

BUSINESS_MODEL_MODIFIERS = {
    "export": {
        "label": "Direct Export",
        "description": "Sell directly to customers in the target country from home",
    },
    "distributor": {
        "label": "Distributor / Partner",
        "description": "Partner with a local company to distribute your products",
    },
    "agent": {
        "label": "Agent / Representative",
        "description": "Appoint a local representative to sell on your behalf",
    },
    "branch": {
        "label": "Branch Office",
        "description": "Open a branch of your home company in the target country",
    },
    "subsidiary": {
        "label": "Local Subsidiary",
        "description": "Register a new company in the target country",
    },
}


# ─────────────────────────────────────────────
# Lookup helpers
# ─────────────────────────────────────────────

JOURNEY_REGISTRY = {
    ("malawi", "zambia"): MALAWI_ZAMBIA_JOURNEY,
    ("zambia", "malawi"): ZAMBIA_MALAWI_JOURNEY,
}


def get_journey_template(origin: str, target: str) -> dict | None:
    """Get the raw journey template for a country pair."""
    return JOURNEY_REGISTRY.get((origin.lower(), target.lower()))


def get_business_model_info(model: str) -> dict:
    """Get display info for a business model."""
    return BUSINESS_MODEL_MODIFIERS.get(model, {"label": model, "description": ""})


SUPPORTED_BUSINESS_MODELS = [
    {"key": k, "label": v["label"], "description": v["description"]}
    for k, v in BUSINESS_MODEL_MODIFIERS.items()
]

SUPPORTED_INDUSTRIES = [
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
