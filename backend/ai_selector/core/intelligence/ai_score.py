class AIScoreEngine:


    def calculate(
         score,
         context=None
    ):

        return (
            score
            *
            context.market_confidence
            *
            confidence
        )