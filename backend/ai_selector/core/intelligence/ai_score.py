from .confidence import calculate_confidence


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


        # 基础因子置信度
        confidence = calculate_confidence(
            factors
        )


        # 市场环境置信度
        if context:

            context_confidence = getattr(
                context,
                "confidence",
                1.0
            )

            confidence *= context_confidence


        return (
            score
            *
            confidence
        )



    @staticmethod
    def calculate_ai_score(
        factors,
        weights=None,
        context=None
    ):

        engine = AIScoreEngine()

        return engine.calculate(
            factors,
            weights,
            context
        )