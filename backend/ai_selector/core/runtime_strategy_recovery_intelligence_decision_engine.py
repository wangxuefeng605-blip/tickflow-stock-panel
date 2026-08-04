class RuntimeStrategyRecoveryIntelligenceDecisionEngine:
    """
    Decision engine for recovery intelligence.
    """

    def __init__(self):

        self.history = []


    def decide(self, recommendation):

        policy = recommendation.get(
            "policy"
        )

        confidence = recommendation.get(
            "confidence",
            0
        )


        if policy is None:

            result = {
                "decision": "reject",
                "policy": None,
                "confidence": 0,
                "risk": 1,
                "execution_ready": False
            }

        else:

            result = {
                "decision": "accept",
                "policy": policy,
                "confidence": confidence,
                "risk": round(
                    1 - confidence,
                    2
                ),
                "execution_ready": True
            }


        self.history.append(
            result
        )

        return result


    def get_history(self):

        return self.history