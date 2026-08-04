class RuntimeStrategyRecoveryDecisionGuardEngine:
    """
    Guard recovery execution according to risk.
    """

    def __init__(self):
        self.history = []


    def guard(self, decision):

        policy = decision.get(
            "policy"
        )

        risk = decision.get(
            "risk",
            1
        )


        if risk < 0.3:

            action = "AUTO_EXECUTE"

        elif risk < 0.7:

            action = "REVIEW_REQUIRED"

        else:

            action = "BLOCK"


        result = {
            "policy": policy,
            "risk": risk,
            "action": action
        }


        self.history.append(
            result
        )


        return result


    def get_history(self):

        return self.history