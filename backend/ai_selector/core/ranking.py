"""
Ranking Engine
v17.2
"""


def rank_stocks(
    results,
    top_n=10,
    weight_provider=None
):

    if not results:
        return []


    for item in results:

        item["final_score"] = (
            calculate_learning_score(
                item,
                weight_provider
            )
        )


    ranked = sorted(
        results,
        key=lambda x:x["final_score"],
        reverse=True
    )


    top = ranked[:top_n]


    for i,item in enumerate(top,1):

        item["rank"]=i


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
            f"Base:{item['score']:.4f} "
            f"Final:{item.get('final_score', item['score']):.4f}"
        )



    print("=" * 50)
def calculate_learning_score(item, provider):

    if provider is None:
        return item["score"]


    factors = item.get(
        "factors",
        {}
    )


    adaptive = 0


    for factor in [
        "momentum",
        "trend",
        "volume_factor",
        "quality",
        "growth",
        "volatility"
    ]:

        value = factors.get(
            factor,
            0
        )

        weight = provider.get_weight(
            factor
        )

        adaptive += (
            value * weight
        )


    

    def save_full_ranking(results):

        import json
        import csv
        from pathlib import Path


        path = Path(
            "data/reports"
        )

        path.mkdir(
            parents=True,
            exist_ok=True
        )


        json_path = (
            path /
            "all_ranked.json"
        )

        csv_path = (
            path /
            "all_ranked.csv"
        )


        with open(
            json_path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                results,
                f,
                ensure_ascii=False,
                indent=2
            )


        if results:

            with open(
                csv_path,
                "w",
                newline="",
                encoding="utf-8"
            ) as f:

                writer = csv.DictWriter(
                    f,
                    fieldnames=results[0].keys()
                )

                writer.writeheader()

                writer.writerows(results)


        return {
            "json": json_path,
            "csv": csv_path
        }