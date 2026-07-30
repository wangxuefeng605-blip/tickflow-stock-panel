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



    def run(
        self,
        ranked
    ):

        ranked = sorted(
            ranked,
            key=lambda x: x.get(
                "score",
                0
            ),
            reverse=True
        )


        output = []


        for index, item in enumerate(
            ranked,
            start=1
        ):

            item = self._inject_weight(
                item
            )


            output.append(
                RankingResult(

                    code=item["code"],

                    score=item["score"],

                    rank=index,

                    factors=item.get(
                        "factors",
                        {}
                    )

                )
            )


        return output

    def _inject_weight(
        self,
        item
    ):

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


        return item