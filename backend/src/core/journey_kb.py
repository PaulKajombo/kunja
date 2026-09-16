"""Journey Knowledge Base for Kunja. Re-export shim.

Data lives in the ``src.core.kb`` package so each module stays under
the 250-line guideline; this module keeps the public import path stable.
"""
from src.core.kb.industry_modifiers import INDUSTRY_MODIFIERS, SUPPORTED_INDUSTRIES
from src.core.kb.business_models import (
    BUSINESS_MODEL_MODIFIERS,
    get_business_model_info,
    SUPPORTED_BUSINESS_MODELS,
)
from src.core.kb.journeys import (
    MALAWI_ZAMBIA_JOURNEY,
    ZAMBIA_MALAWI_JOURNEY,
    JOURNEY_REGISTRY,
    get_journey_template,
)
