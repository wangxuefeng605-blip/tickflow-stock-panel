class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionPredictiveRiskControlEngine:
    """
    Predictive risk management engine.
    """

    def __init__(self):

        self.risk_state = {}

        self.history = []



    def evaluate_prediction(
        self,
        prediction,
        confidence
    ):

        if prediction == "BEAR_RISK" and confidence > 0.6:

            action = "REDUCE_EXPOSURE"


        elif prediction == "BULL_CONTINUATION":

            action = "MAINTAIN_EXPOSURE"


        else:

            action = "NEUTRAL"



        result = {

            "prediction": prediction,

            "confidence": confidence,

            "action": action

        }


        self.risk_state = result


        self.history.append(
            {
                "action": "evaluate",
                "result": result
            }
        )


        return result



    def calculate_exposure(
        self,
        current_weight
    ):

        action = self.risk_state.get(
            "action"
        )


        if action == "REDUCE_EXPOSURE":

            new_weight = round(
                current_weight * 0.5,
                3
            )


        elif action == "MAINTAIN_EXPOSURE":

            new_weight = current_weight


        else:

            new_weight = round(
                current_weight * 0.8,
                3
            )


        result = {

            "old_weight": current_weight,

            "new_weight": new_weight

        }


        self.history.append(
            {
                "action": "adjust",
                "result": result
            }
        )


        return result



    def get_history(self):

        return self.history