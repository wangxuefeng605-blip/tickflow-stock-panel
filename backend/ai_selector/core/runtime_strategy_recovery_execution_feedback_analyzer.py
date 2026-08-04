class RuntimeStrategyRecoveryExecutionFeedbackAnalyzer:
    """
    Analyze recovery execution feedback.
    """

    def __init__(self):

        self.history = []


    def analyze(self, execution_result):

        status = execution_result.get(
            "status"
        )

        action = execution_result.get(
            "action"
        )


        if status == "executed":

            success_score = 1.0

            recovery_quality = "positive"

            learning_signal = 1


        elif status == "blocked":

            success_score = 0.0

            recovery_quality = "blocked"

            learning_signal = -1


        else:

            success_score = 0.2

            recovery_quality = "unknown"

            learning_signal = 0


        result = {
            "action": action,
            "success_score": success_score,
            "recovery_quality": recovery_quality,
            "learning_signal": learning_signal
        }


        self.history.append(
            result
        )


        return result


    def get_history(self):

        return self.history