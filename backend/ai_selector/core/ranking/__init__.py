from .ranker import Ranker
from .pipeline import RankingPipeline
from .types import RankingResult
from core.learning.weight_provider import LearningWeightProvider



def rank_stocks(
    results,
    top_n=10,
    weight_provider=None
):

    pipeline = RankingPipeline(
        weight_provider
    )

    ranked = pipeline.run(
        results
    )

    return ranked[:top_n]



def print_top10(results):

    print("=" * 50)
    print(" AI TOP10 INTELLIGENT RANKING ")
    print("=" * 50)


    for item in results[:10]:

        print()

        print(
            f"{item.rank}. {item.code}"
        )

        print(
            f"Score: {item.score:.4f}"
        )


        print()
        print("Market:")

        market = (
            item.explanation.get(
                "market_state",
                "UNKNOWN"
            )
            if item.explanation
            else "UNKNOWN"
        )

        print(
            market
        )


        print()

        print("Confidence:")

        confidence = (
            item.explanation.get(
                "confidence",
                0
            )
            if item.explanation
            else 0
        )

        print(
            round(
                confidence,
                2
            )
        )


        print()

        print("Signals:")

        for signal in item.signals:

            print(
                f" - {signal}"
            )


        print()

        print("Reason:")

        if item.explanation:

            summary = item.explanation.get(
                "summary",
                ""
            )

            if not summary:

                nested = item.explanation.get(
                    "explanation",
                    {}
                )

                summary = nested.get(
                    "summary",
                    ""
                )


            print(
                summary.strip()
            )

        else:

            print(
                "None"
            )



    print("=" * 50)

def rank_stocks(
    results,
    top_n=10,
    weight_provider=None
):

    ranked = RankingPipeline(
        weight_provider=weight_provider
    ).run(results)

    return ranked[:top_n]