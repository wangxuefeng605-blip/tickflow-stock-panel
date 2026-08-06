"""
AI Performance Summary

Generate performance statistics.
"""

import json
from pathlib import Path


PERFORMANCE_DIR = Path(
    "data/performance"
)


def load_latest():

    files = sorted(
        PERFORMANCE_DIR.glob("*.json")
    )

    if not files:
        return None


    with open(
        files[-1],
        "r",
        encoding="utf-8"
    ) as f:

        return json.load(f)



def generate_summary():

    data = load_latest()


    if data is None:

        return None


    results = data.get(
        "results",
        []
    )


    total = len(results)


    wins = [

        x for x in results

        if x.get("win")

    ]


    loses = total - len(wins)


    returns = [

        x.get("return_1d")

        for x in results

        if x.get("return_1d") is not None

    ]


    avg_return = (

        sum(returns)
        /
        len(returns)

        if returns

        else 0

    )


    best = max(
        results,
        key=lambda x:x.get(
            "return_1d",
            -999
        )
    )


    worst = min(
        results,
        key=lambda x:x.get(
            "return_1d",
            999
        )
    )


    summary = {

        "date":
            data.get("date"),


        "total":
            total,


        "wins":
            len(wins),


        "loses":
            loses,


        "win_rate":
            round(
                len(wins)
                /
                total,
                4
            ),


        "average_return":
            round(
                avg_return,
                4
            ),


        "best":
            best,


        "worst":
            worst

    }


    return summary



if __name__ == "__main__":

    print(
        json.dumps(
            generate_summary(),
            indent=2,
            ensure_ascii=False
        )
    )