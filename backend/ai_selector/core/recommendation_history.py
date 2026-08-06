"""
AI Recommendation History

Store daily AI TOP10 recommendations.
"""

import json
from pathlib import Path
from datetime import datetime


HISTORY_DIR = Path(
    "data/history/ai_recommendations"
)


def save_daily_recommendation(
    data
):
    """
    Save AI TOP10 recommendation.
    """

    HISTORY_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    filename = (
        datetime.now()
        .strftime("%Y%m%d")
        +
        ".json"
    )


    output = (
        HISTORY_DIR /
        filename
    )


    record = {

        "date":
            datetime.now()
            .strftime("%Y-%m-%d"),


        "created_at":
            datetime.now()
            .isoformat(),


        "count":
            len(data),


        "recommendations":
            data

    }


    with open(
        output,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            record,
            f,
            ensure_ascii=False,
            indent=2
        )


    return output



def load_history():

    if not HISTORY_DIR.exists():

        return []


    result = []


    for file in sorted(
        HISTORY_DIR.glob("*.json")
    ):

        with open(
            file,
            "r",
            encoding="utf-8"
        ) as f:

            result.append(
                json.load(f)
            )


    return result



def get_latest():

    history = load_history()


    if not history:

        return None


    return history[-1]