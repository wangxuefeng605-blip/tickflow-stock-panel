class RuntimeStrategyRecoveryFeedbackLearningIntegrator:
    """
    Integrate recovery feedback into strategy learning.
    """

    def __init__(self):
        self.learning_history = []


    def integrate_feedback(self, feedback):

        if not feedback:
            return None


        policy = feedback.get(
            "policy"
        )

        success = feedback.get(
            "success"
        )


        if success:
            weight = 1.1
        else:
            weight = 0.9


        learning_signal = {
            "policy": policy,
            "learning_weight": weight,
            "updated": True
        }


        self.learning_history.append(
            learning_signal
        )


        return learning_signal



    def history(self):

        return self.learning_history