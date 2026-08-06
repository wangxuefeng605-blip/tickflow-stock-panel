"""
Portfolio Feedback Collector

Convert AI recommendations into learning feedback records.
"""


import json

from pathlib import Path
from datetime import datetime


OUTCOME_DIR = Path(
    "data/learning/outcomes"
)


OUTCOME_DIR.mkdir(
    parents=True,
    exist_ok=True
)



def create_feedback_record(
    recommendation
):
    """
    Create portfolio feedback record.
    """

    return {

        "code":
            recommendation.get("code"),

        "recommend_score":
            recommendation.get(
                "score",
                0
            ),

        "alpha_score":
            recommendation.get(
                "alpha_score",
                0
            ),

        "recommend_date":
            datetime.now()
            .strftime(
                "%Y-%m-%d"
            ),

        "status":
            "PENDING"

    }



def save_feedback(
    records
):

    path = (
        OUTCOME_DIR
        /
        (
            datetime.now()
            .strftime("%Y%m%d")
            +
            ".json"
        )
    )


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            records,
            f,
            indent=4,
            ensure_ascii=False
        )


    return path