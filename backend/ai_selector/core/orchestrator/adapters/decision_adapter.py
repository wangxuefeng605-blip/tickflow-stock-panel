from types import SimpleNamespace


class DecisionAdapter:


    def __init__(
        self,
        engine
    ):

        self.engine = engine



    def run(
        self,
        ranking
    ):

        decisions = []


        context = SimpleNamespace(
            market_state=self._market_state(ranking)
        )


        for item in ranking:

            data = self._convert(
                item
            )


            decision = self.engine.decide(
                data,
                context
            )


            decisions.append(
                decision
            )


        return decisions



    def _convert(
        self,
        item
    ):

        return {

            "code": item.code,

            "score": item.score,

            "confidence": item.confidence

        }



    def _market_state(
        self,
        ranking
    ):

        if not ranking:

            return "UNKNOWN"


        return ranking[0].market_state