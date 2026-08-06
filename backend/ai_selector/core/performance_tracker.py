"""
AI Recommendation Performance Tracker

Track historical AI TOP10 performance.
"""

import json
from pathlib import Path
from datetime import datetime


HISTORY_DIR = Path(
    "data/history/ai_recommendations"
)


PERFORMANCE_DIR = Path(
    "data/performance"
)


def load_latest_recommendation():

    files = sorted(
        HISTORY_DIR.glob("*.json")
    )


    if not files:
        return None


    latest = files[-1]


    with open(
        latest,
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def calculate_return(
    buy_price,
    current_price
):

    if buy_price == 0:

        return 0


    return (
        current_price - buy_price
    ) / buy_price



def generate_performance_report(
    results
):

    PERFORMANCE_DIR.mkdir(
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
        PERFORMANCE_DIR /
        filename
    )


    report = {

        "date":
            datetime.now()
            .strftime("%Y-%m-%d"),


        "count":
            len(results),


        "results":
            results

    }


    with open(
        output,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            report,
            f,
            ensure_ascii=False,
            indent=2
        )


    return output



def run_tracker():

    history = load_latest_recommendation()


    if history is None:

        return None


    recommendations = (
        history.get(
            "recommendations",
            []
        )
    )


    results = []


    for item in recommendations:

        results.append(

            {

                "code":
                    item.get("code"),


                "score":
                    item.get("score"),


                "return_1d":
                    None

            }

        )


    return generate_performance_report(
        results
    )



if __name__ == "__main__":

    print(
        run_tracker()
    )