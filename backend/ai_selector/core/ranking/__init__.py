from .types import RankingResult
from .ranker import Ranker
from .pipeline import RankingPipeline


def rank_stocks(
    data,
    learning_pipeline=None,
    top_n=None,
    weights=None,
    weight_provider=None
):
    """
    Public ranking entry point.

    Flow:

        scan results
            ↓
        optional learning pipeline
            ↓
        resolve weights
            ↓
        apply factor weights
            ↓
        Ranker
            ↓
        RankingResult
    """

    if not data:
        return []

    # -------------------------------------------------
    # 1. Keep dictionary scan results only
    # -------------------------------------------------

    data = [
        item
        for item in data
        if isinstance(item, dict)
    ]

    if not data:
        return []

    # -------------------------------------------------
    # 2. Learning pipeline
    # -------------------------------------------------

    if learning_pipeline:

        if hasattr(
            learning_pipeline,
            "apply"
        ):

            data = learning_pipeline.apply(
                data
            )

        elif hasattr(
            learning_pipeline,
            "run"
        ):

            data = learning_pipeline.run(
                data
            )

        if data is None:
            return []

    # -------------------------------------------------
    # 3. Resolve weight provider
    # -------------------------------------------------

    if weights is None and weight_provider:

        if hasattr(
            weight_provider,
            "get_weights"
        ):

            weights = (
                weight_provider
                .get_weights()
            )

        elif hasattr(
            weight_provider,
            "get_weight"
        ):

            weights = {}

            factors = set()

            for item in data:

                factors.update(
                    item.get(
                        "factors",
                        {}
                    ).keys()
                )

            for factor in factors:

                weights[factor] = (
                    weight_provider
                    .get_weight(
                        factor
                    )
                )

    if weights is None:

        weights = {}

    # -------------------------------------------------
    # 4. Apply weights
    # -------------------------------------------------

    if weights:

        adjusted = []

        for item in data:

            factors = item.get(
                "factors",
                {}
            )

            weighted_score = sum(

                value
                *
                weights.get(
                    name,
                    0.0
                )

                for name, value
                in factors.items()
            )

            new_item = dict(item)

            # Preserve original scanner / AI score.
            new_item["alpha_score"] = item.get(
                "alpha_score",
                item.get(
                    "score",
                    0.0
                )
            )

            # Ranking score after learned weights.
            new_item["score"] = (
                weighted_score
            )

            new_item["final_score"] = (
                weighted_score
            )

            new_item["weights"] = {

                name: weights.get(
                    name,
                    0.0
                )

                for name in factors
            }

            adjusted.append(
                new_item
            )

        data = adjusted

    else:

        # No ranking weights supplied.
        # Preserve existing scanner score.
        for item in data:

            item.setdefault(
                "alpha_score",
                item.get(
                    "score",
                    0.0
                )
            )

            item.setdefault(
                "final_score",
                item.get(
                    "score",
                    0.0
                )
            )

            item["weights"] = {}

    # -------------------------------------------------
    # 5. Rank
    # -------------------------------------------------

    ranker = Ranker()

    results = ranker.rank(
        data
    )

    if results is None:
        return []

    # -------------------------------------------------
    # 6. Top N
    # -------------------------------------------------

    if top_n is not None:

        return results[:top_n]

    return results


def print_top10(results):

    for item in results[:10]:

        if hasattr(
            item,
            "rank"
        ):

            print(
                f"{item.rank}. "
                f"{item.code} "
                f"{item.score}"
            )

        elif isinstance(
            item,
            dict
        ):

            print(
                f"{item.get('rank')}. "
                f"{item.get('code')} "
                f"{item.get('score')}"
            )

        else:

            print(
                item
            )