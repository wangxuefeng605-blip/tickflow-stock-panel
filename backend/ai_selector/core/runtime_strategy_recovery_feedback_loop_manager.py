class RuntimeStrategyRecoveryFeedbackLoopManager:
    """
    Collect recovery execution feedback
    and provide learning signals.
    """

    def __init__(self):
        self.history = []


    def collect_feedback(self, execution_result):

        if not execution_result:
            return None


        status = execution_result.get(
            "status"
        )

        success = status == "executed"


        feedback = {
            "policy": execution_result.get(
                "policy"
            ),
            "success": success,
            "feedback_score": 1.0 if success else 0.0
        }


        self.history.append(
            feedback
        )


        return feedback



    def feedback_history(self):

        return self.history