class RuntimeStrategyRecoveryFeedbackLearningController:
    """
    Controller for runtime strategy recovery feedback learning.
    """

    def __init__(self):

        self.history = []


    def process(self, feedback):

        policy = feedback.get(
            "policy",
            "unknown"
        )

        success = feedback.get(
            "success",
            False
        )

        confidence = feedback.get(
            "confidence",
            0
        )


        result = {
            "status": "learning",
            "policy": policy,
            "success": success,
            "confidence": confidence
        }


        self.history.append(
            result
        )


        return result


    def get_history(self):

        return self.history