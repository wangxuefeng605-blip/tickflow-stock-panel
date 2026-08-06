"""
AI Feedback Learning Engine

Analyze recommendation performance
and generate weight suggestions.
"""

import json
from pathlib import Path
from datetime import datetime
from core.learning.decision_engine import (
    LearningDecisionEngine
)

PERFORMANCE_DIR = Path(
    "data/performance"
)


LEARNING_DIR = Path(
    "data/learning"
)


DEFAULT_WEIGHTS = {

    "momentum": 0.35,

    "trend": 0.30,

    "quality": 0.15,

    "liquidity": 0.10,

    "risk": 0.10

}



def load_latest_performance():

    files = sorted(
        PERFORMANCE_DIR.glob("*.json")
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





def calculate_learning_signal(data):

    """
    Calculate simple learning signal.

    First version:
    only use win rate and average return.
    """


    results = data.get(
        "results",
        []
    )


    if not results:

        return 0



    wins = sum(

        1

        for x in results

        if x.get("win")

    )


    total = len(results)


    win_rate = wins / total


    avg_return = sum(

        x.get(
            "return_1d",
            0
        )

        for x in results

    ) / total



    signal = (

        win_rate * 0.6

        +

        avg_return * 0.4

    )


    return round(
        signal,
        4
    )





def adjust_weights(signal):


    weights = DEFAULT_WEIGHTS.copy()



    if signal > 0.5:

        weights["momentum"] += 0.05

        weights["trend"] += 0.03



    elif signal < 0.3:

        weights["risk"] += 0.05

        weights["quality"] += 0.03



    total = sum(
        weights.values()
    )


    for k in weights:

        weights[k] = round(
            weights[k] / total,
            4
        )


    return weights





def generate_learning_report():


    data = load_latest_performance()


    if not data:

        return None



    signal = calculate_learning_signal(
        data
    )


    weights = adjust_weights(
        signal
    )



    report = {

        "date":
            datetime.now()
            .strftime("%Y-%m-%d"),


        "learning_signal":
            signal,


        "suggested_weights":
            weights

    }



    LEARNING_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    output = (
        LEARNING_DIR /
        "weight_adjustment.json"
    )


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





def run_learning():

    return generate_learning_report()



if __name__ == "__main__":

    print(
        run_learning()
    )