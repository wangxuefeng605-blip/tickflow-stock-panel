from core.decision import (
    DecisionEngine,
    DecisionStore
)

from core.ranking.types import RankingResult



class DecisionPipeline:


    def __init__(
        self,
        engine=None,
        store=None
    ):

        self.engine = (
            engine
            or DecisionEngine()
        )

        self.store = (
            store
            or DecisionStore()
        )



    def normalize(
        self,
        item
    ):


        if isinstance(
            item,
            dict
        ):

            return RankingResult(

                code=item["code"],

                score=item.get(
                    "score",
                    0
                ),

                confidence=item.get(
                    "confidence",
                    0
                ),

                market_state=item.get(
                    "market_state",
                    "UNKNOWN"
                )

            )


        return item



    def run(
        self,
        ranking
    ):

        decisions = []


        for item in ranking:


            item = self.normalize(
                item
            )


            decision = self.engine.decide(
                item
            )


            self.store.save(
                decision
            )


            decisions.append(
                decision
            )


        return decisions