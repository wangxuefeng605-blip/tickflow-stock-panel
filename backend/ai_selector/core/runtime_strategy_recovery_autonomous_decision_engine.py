class RuntimeStrategyRecoveryAutonomousDecisionEngine:
    """
    Autonomous recovery decision engine.
    """

    def __init__(self):

        self.history = []


    def decide(self, runtime_state):

        confidence = runtime_state.get(
            "confidence",
            0.5
        )

        risk = round(
            1 - confidence,
            2
        )


        if confidence >= 0.7:
            policy = "restore"

        elif confidence >= 0.4:
            policy = "fallback"

        else:
            policy = "rollback"


        allowed = risk < 0.5


        result = {
            "policy": policy,
            "confidence": confidence,
            "risk": risk,
            "approved": allowed
        }


        self.history.append(
            result
        )


        return result


    def get_history(self):

        return self.history