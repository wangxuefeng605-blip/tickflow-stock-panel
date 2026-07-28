from .ranker import Ranker
from .pipeline import RankingPipeline
from .types import RankingResult


def rank_stocks(results, top_n=10):

    ranked = RankingPipeline().run(results)

    return ranked[:top_n]

    return RankingPipeline().run(results)



def print_top10(results):

    print("=" * 50)
    print(" AI TOP10 INTELLIGENT RANKING ")
    print("=" * 50)


    for item in results[:10]:

        print(
            "DEBUG RESULT:",
            item
        )
        
        print(
             "DEBUG EXPLANATION:",
             item.explanation
      )
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


            if item.explanation:

                print()

                print(
                    "Market:",
                    item.explanation.get(
                        "market_state",
                        "UNKNOWN"
                    )
                )


                print(
                    "Confidence:",
                    item.explanation.get(
                        "confidence",
                        0
                    )
                )


                print(
                    "Reason:"
                )


                summary = item.explanation.get(
                    "summary",
                    ""
                )


                print(
                    summary.strip()
                )


    print("=" * 50)