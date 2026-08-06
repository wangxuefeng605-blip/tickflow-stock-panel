"""
AI Weight Provider

Load learning generated weights.
Fallback to default weights.
"""

import json
from pathlib import Path


WEIGHT_FILE = Path(
    "data/learning/weight_adjustment.json"
)


DEFAULT_WEIGHTS = {

    "momentum": 0.35,

    "trend": 0.30,

    "quality": 0.15,

    "liquidity": 0.10,

    "risk": 0.10

}



def get_ai_weights():

    """
    Load AI learned weights.

    fallback:
        DEFAULT_WEIGHTS
    """


    if not WEIGHT_FILE.exists():

        return DEFAULT_WEIGHTS.copy()


    try:

        with open(
            WEIGHT_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        weights = data.get(
            "suggested_weights"
        )


        if not weights:

            return DEFAULT_WEIGHTS.copy()


        result = DEFAULT_WEIGHTS.copy()


        result.update(
            weights
        )


        return result


    except Exception:

        return DEFAULT_WEIGHTS.copy()