class RuntimeStrategyRecoveryIntelligenceAutonomousDecisionEngine:
    """
    Autonomous recovery decision engine.
    """

    def __init__(self):

        self.history = []


    def decide(self, context):

        policy = context.get(
            "policy",
            "restore"
        )

        confidence = context.get(
            "confidence",
            0.5
        )

        risk = round(
            1 - confidence,
            2
        )


        allowed = (
            confidence >= 0.5
            and risk <= 0.5
        )


        result = {

            "action": (
                "execute"
                if allowed
                else "reject"
            ),

            "policy": policy,

            "confidence": confidence,

            "risk": risk,

            "allowed": allowed

        }


        self.history.append(result)

        return result


    def get_history(self):

        return self.history