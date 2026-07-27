class AIScoreEngine:


    def calculate(
        self,
        factors,
        weights=None,
        context=None
    ):


        if weights is None:

            weights = {
                "momentum": 0.25,
                "trend": 0.25,
                "quality": 0.20,
                "liquidity": 0.15,
                "risk": 0.15
            }


        score = 0


        for key, weight in weights.items():

            value = factors.get(
                key,
                0
            )

            score += (
                value
                *
                weight
            )


        confidence = 1.0


        if context:

            confidence = (
                getattr(
                    context,
                    "confidence",
                    1.0
                )
            )


        return (
            score
            *
            confidence
        )