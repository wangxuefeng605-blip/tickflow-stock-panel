from .ranker import Ranker
from .pipeline import RankingPipeline
from .types import RankingResult


def rank_stocks(
    results,
    top_n=10
):

    return RankingPipeline().run(results)



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


        print(
            "Signals:"
        )

        for s in item.signals:

            print(
                f" - {s}"
            )


        if hasattr(item, "explanation"):

            print(
                "Explanation:"
            )

            print(
                item.explanation
            )


    print("=" * 50)