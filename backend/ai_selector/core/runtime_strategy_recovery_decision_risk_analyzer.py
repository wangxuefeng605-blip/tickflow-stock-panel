class RuntimeStrategyRecoveryDecisionRiskAnalyzer:
    """
    Analyze recovery decision risk.
    """

    def __init__(self):
        self.history = []


    def analyze(
        self,
        decision
    ):

        policy = decision.get(
            "selected_policy"
        )

        confidence = decision.get(
            "confidence",
            0
        )


        risk = round(1 - confidence, 2)


        if risk < 0.3:
            level = "LOW"

        elif risk < 0.7:
            level = "MEDIUM"

        else:
            level = "HIGH"


        result = {
            "policy": policy,
            "risk": risk,
            "risk_level": level
        }


        self.history.append(
            result
        )


        return result


    def get_history(self):

        return self.history