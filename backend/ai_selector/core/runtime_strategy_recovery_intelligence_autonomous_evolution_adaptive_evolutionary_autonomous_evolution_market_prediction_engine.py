class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionMarketPredictionEngine:
    """
    Predicts future market conditions.
    """

    def __init__(self):

        self.predictions = []

        self.history = []



    def predict(
        self,
        momentum_change,
        trend_strength,
        volatility_change
    ):

        score = (
            momentum_change * 0.4
            +
            trend_strength * 0.5
            -
            volatility_change * 0.1
        )


        if score > 0.6:

            prediction = "BULL_CONTINUATION"


        elif score < 0.3:

            prediction = "BEAR_RISK"


        else:

            prediction = "UNCERTAIN"



        result = {

            "prediction": prediction,

            "confidence": round(
                abs(score - 0.5) + 0.5,
                3
            )

        }


        self.predictions.append(
            result
        )


        self.history.append(
            {
                "action": "predict",
                "result": result
            }
        )


        return result



    def latest_prediction(self):

        if not self.predictions:

            return None


        return self.predictions[-1]



    def get_history(self):

        return self.history