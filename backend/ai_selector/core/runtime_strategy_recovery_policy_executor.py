class RuntimeStrategyRecoveryPolicyExecutor:
    """
    Execute selected recovery policy.
    """

    def __init__(self):
        self.history = []


    def execute(self, policy_result):

        if not policy_result:
            return None


        policy = policy_result.get(
            "selected_policy"
        )


        if policy not in [
            "fallback",
            "rollback",
            "parameter_restore"
        ]:
            result = {
                "policy": policy,
                "status": "failed"
            }

        else:
            result = {
                "policy": policy,
                "status": "executed"
            }


        self.history.append(
            result
        )


        return result



    def execution_history(self):

        return self.history