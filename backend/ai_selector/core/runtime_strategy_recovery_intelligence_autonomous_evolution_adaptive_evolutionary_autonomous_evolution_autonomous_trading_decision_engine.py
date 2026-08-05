class RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionAutonomousTradingDecisionEngine:
    """
    Generates autonomous trading decisions.
    """

    def __init__(self):

        self.decisions = []

        self.history = []



    def decide(
        self,
        prediction,
        risk_action,
        score
    ):

        if (
            prediction == "BULL_CONTINUATION"
            and
            risk_action == "MAINTAIN_EXPOSURE"
            and
            score >= 0.7
        ):

            action = "BUY"


        elif risk_action == "REDUCE_EXPOSURE":

            action = "SELL"


        else:

            action = "HOLD"



        result = {

            "action": action,

            "score": score,

            "prediction": prediction,

            "risk_action": risk_action

        }


        self.decisions.append(
            result
        )


        self.history.append(
            {
                "action": "decision",
                "result": result
            }
        )


        return result



    def position_size(
        self,
        score,
        risk_level
    ):

        size = score * (1 - risk_level)


        result = round(
            max(
                min(size, 1),
                0
            ),
            3
        )


        self.history.append(
            {
                "action": "position",
                "size": result
            }
        )


        return result



    def latest_decision(self):

        if not self.decisions:

            return None


        return self.decisions[-1]



    def get_history(self):

        return self.history