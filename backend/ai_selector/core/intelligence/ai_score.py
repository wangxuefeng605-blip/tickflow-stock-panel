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
    if weights is None:

    weights = {
        "momentum":0.25,
        "trend":0.25,
        "quality":0.20,
        "liquidity":0.15,
        "risk":0.15
    }