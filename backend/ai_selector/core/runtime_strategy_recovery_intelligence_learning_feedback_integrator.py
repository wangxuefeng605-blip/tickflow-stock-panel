class RuntimeStrategyRecoveryIntelligenceLearningFeedbackIntegrator:
    """
    Integrates recovery execution feedback into learning memory.
    """

    def __init__(self):

        self.history = []
        self.experience_memory = []


    def integrate(self, feedback):

        if feedback.get("learning_feedback") == "positive":

            update = {
                "learning_signal": "reward",
                "weight_delta": 0.1,
                "experience": "successful_recovery"
            }

        else:

            update = {
                "learning_signal": "penalty",
                "weight_delta": -0.1,
                "experience": (
                    feedback.get(
                        "failure_reason",
                        "unknown_failure"
                    )
                )
            }


        self.experience_memory.append(update)
        self.history.append(update)

        return update


    def get_history(self):

        return self.history


    def get_memory(self):

        return self.experience_memory