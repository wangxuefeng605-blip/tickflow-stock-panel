from .ranker import Ranker
from .explain import explain
from types import SimpleNamespace
from core.ranking.types import RankingResult


class RankingPipeline:


    def __init__(
        self,
        weight_provider=None
    ):

        self.weight_provider = weight_provider



    from .types import RankingResult


    def run(self, results):


        ranked = [
            item
            for item in results
            if isinstance(item, dict)
        ]


        for item in ranked:
            self._inject_weight(item)


        ranked = sorted(
            ranked,
            key=lambda x: self._adaptive_score(x),
            reverse=True
        )
        


        output = []


        for index, item in enumerate(
            ranked,
            start=1
        ):

            output.append(

                RankingResult(

                    code=item["code"],

                    score=item.get(
                        "score",
                        item.get(
                            "alpha_score",
                            0
                        )
                    ),

                    rank=index,

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


        if self.weight_provider is None:
            return base_score


        factors = item.get(
            "factors",
            {}
        )


        total = base_score


        for factor, value in factors.items():

            weight = self.weight_provider.get_weight(
                factor
            )

            total += value * weight


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


            print(
                "FINAL WEIGHT:",
                item["code"],
                item.get("learning_weight")
            )
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


        learning_weight = 1


        for factor, weight in weights.items():

            learning_weight *= weight


        item["learning_weight"] = learning_weight


        return item