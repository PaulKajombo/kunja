"""Assembled journey templates for each country pair."""
from src.core.kb.mz_p0 import PHASE as MZ_P0
from src.core.kb.mz_p1 import PHASE as MZ_P1
from src.core.kb.mz_p2 import PHASE as MZ_P2
from src.core.kb.mz_p3 import PHASE as MZ_P3
from src.core.kb.mz_p4 import PHASE as MZ_P4
from src.core.kb.mz_p5 import PHASE as MZ_P5
from src.core.kb.zm_p0 import PHASE as ZM_P0
from src.core.kb.zm_p1 import PHASE as ZM_P1
from src.core.kb.zm_p2 import PHASE as ZM_P2
from src.core.kb.zm_p3 import PHASE as ZM_P3
from src.core.kb.zm_p4 import PHASE as ZM_P4
from src.core.kb.zm_p5 import PHASE as ZM_P5

MALAWI_ZAMBIA_JOURNEY = {
    'origin': 'malawi',
    'target': 'zambia',
    'origin_name': 'Malawi',
    'target_name': 'Zambia',
    'origin_flag': '🇲🇼',
    'target_flag': '🇿🇲',
    "phases": [MZ_P0, MZ_P1, MZ_P2, MZ_P3, MZ_P4, MZ_P5],
}

ZAMBIA_MALAWI_JOURNEY = {
    'origin': 'zambia',
    'target': 'malawi',
    'origin_name': 'Zambia',
    'target_name': 'Malawi',
    'origin_flag': '🇿🇲',
    'target_flag': '🇲🇼',
    "phases": [ZM_P0, ZM_P1, ZM_P2, ZM_P3, ZM_P4, ZM_P5],
}

JOURNEY_REGISTRY = {
    ("malawi", "zambia"): MALAWI_ZAMBIA_JOURNEY,
    ("zambia", "malawi"): ZAMBIA_MALAWI_JOURNEY,
}


def get_journey_template(origin: str, target: str) -> dict | None:
    """Get the raw journey template for a country pair."""
    return JOURNEY_REGISTRY.get((origin.lower(), target.lower()))
