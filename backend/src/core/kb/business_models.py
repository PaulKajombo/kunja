"""Business model display info and supported models."""

BUSINESS_MODEL_MODIFIERS = BUSINESS_MODEL_MODIFIERS = {
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



def get_business_model_info(model: str) -> dict:
    """Get display info for a business model."""
    return BUSINESS_MODEL_MODIFIERS.get(model, {"label": model, "description": ""})


SUPPORTED_BUSINESS_MODELS = [
    {"key": k, "label": v["label"], "description": v["description"]}
    for k, v in BUSINESS_MODEL_MODIFIERS.items()
]
