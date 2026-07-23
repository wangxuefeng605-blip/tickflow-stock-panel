"""
Ranking Engine
v17.2
"""


def rank_stocks(results, top_n=10):

    if not results:
        return []


    ranked = sorted(
        results,
        key=lambda x: x["score"],
        reverse=True
    )


    top = ranked[:top_n]


    for i, item in enumerate(top, 1):
        item["rank"] = i


    return top



def print_top10(results):

    print()

    print("=" * 50)
    print(" AI TOP10 STOCK RANKING ")
    print("=" * 50)


    for item in results:

        print(
            f"{item['rank']:>2}. "
            f"{item['code']} "
            f"Score: {item['score']:.4f}"
        )


    print("=" * 50)