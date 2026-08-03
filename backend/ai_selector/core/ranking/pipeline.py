from .ranker import Ranker
from .explain import explain
from core.ranking.types import RankingResult


class RankingPipeline:


    def __init__(
        self,
        weight_provider=None,
        stock_weight_provider=None
    ):

        self.weight_provider = weight_provider

        self.stock_weight_provider = (
            stock_weight_provider
        )


    def run(
        self,
        results
    ):

        ranked = [
            item
            for item in results
            if isinstance(item, dict)
        ]


        for item in ranked:
            self._inject_weight(item)


        print(
            "BEFORE SORT"
        )


        for item in ranked[:5]:

            print(
                item.get("code"),
                item.get("score"),
                item.get("alpha_score")
            )


        ranked = sorted(
            ranked,
            key=lambda x: self._adaptive_score(x),
            reverse=True
        )


        print(
            "AFTER SORT"
        )


        for item in ranked[:10]:

            print(
                item.get("code"),
                self._adaptive_score(item)
            )


        output = []


        for index, item in enumerate(
            ranked,
            start=1
        ):

            output.append(

                RankingResult(

                    code=item["code"],

                    score=self._adaptive_score(item),

                    rank=index,

                    alpha_score=item.get(
                        "score",
                        item.get(
                            "alpha_score",
                            0
                        )
                    ),

                    factors=item.get(
                        "factors",
                        {}
                    ),

                    signals=item.get(
                        "signals",
                        []
                    ),

                    market_state=item.get(
                        "market_state",
                        "UNKNOWN"
                    ),

                    confidence=item.get(
                        "confidence",
                        0
                    ),

                    explanation=item.get(
                        "explanation",
                        {}
                    ),

                    reason=item.get(
                        "reason",
                        ""
                    )
                )
            )


        return output



    def _adaptive_score(
        self,
        item
    ):


        base_score = item.get(
            "score",
            item.get(
                "alpha_score",
                0
            )
        )


        learning_weight = item.get(
            "learning_weight",
            1.0
        )


        base_score *= learning_weight


        if self.weight_provider is None:

            return base_score


        total = base_score


        factors = item.get(
            "factors",
            {}
        )


        for factor, value in factors.items():

            weight = (
                self.weight_provider.get_weight(
                    factor
                )
            )


            total += (
                value * weight
            )


        return total



    def _inject_weight(
        self,
        item
    ):


        print(
            "INJECT:",
            item["code"]
        )


        if self.weight_provider is None:

            return item



        factors = item.get(
            "factors",
            {}
        )


        weights = {}


        for factor in factors:

            weights[factor] = (
                self.weight_provider.get_weight(
                    factor
                )
            )


        item["weights"] = weights



        learning_weight = 1.0


        if self.stock_weight_provider:

            learning_weight = (
                self.stock_weight_provider.get_weight(
                    item["code"]
                )
            )


        item["learning_weight"] = (
            learning_weight
        )


        print(
            "FINAL WEIGHT:",
            item["code"],
            learning_weight
        )


        return item