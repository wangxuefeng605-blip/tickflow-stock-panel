class RuntimeStrategyRecoveryDecisionExecutionAuditor:
    """
    Audit recovery decision execution.
    """

    def __init__(self):
        self.history = []


    def audit(self, execution):

        policy = execution.get(
            "policy"
        )

        action = execution.get(
            "action"
        )

        risk = execution.get(
            "risk",
            1
        )


        status = "AUDITED"


        result = {
            "policy": policy,
            "action": action,
            "risk": risk,
            "status": status
        }


        self.history.append(
            result
        )


        return result


    def get_history(self):

        return self.history