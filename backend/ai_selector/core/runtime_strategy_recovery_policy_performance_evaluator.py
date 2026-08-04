class RuntimeStrategyRecoveryPolicyPerformanceEvaluator:
    """
    Evaluate recovery policy performance.
    """

    def __init__(self):
        self.history = []


    def evaluate(
        self,
        policy,
        success,
        failure,
        avg_recovery_time=0
    ):

        total = success + failure

        if total == 0:
            success_rate = 0
        else:
            success_rate = success / total


        stability_factor = (
            1 / (1 + avg_recovery_time)
        )


        failure_penalty = (
            failure / total
            if total > 0
            else 0
        )


        score = (
            success_rate
            + stability_factor
            - failure_penalty
        )


        result = {
            "policy": policy,
            "score": score,
            "success_rate": success_rate
        }


        self.history.append(result)

        return result


    def get_history(self):

        return self.history