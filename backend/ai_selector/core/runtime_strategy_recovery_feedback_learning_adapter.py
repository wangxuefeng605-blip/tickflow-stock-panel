class RuntimeStrategyRecoveryFeedbackLearningAdapter:
    """
    Convert recovery feedback into learning signals.
    """

    def __init__(self):
        self.history = []


    def adapt(self, feedback):

        policy = feedback.get(
            "policy"
        )

        result = feedback.get(
            "feedback",
            "NEUTRAL"
        )


        if result == "POSITIVE":

            score = 1.0

        elif result == "NEGATIVE":

            score = -1.0

        else:

            score = 0.0


        record = {
            "policy": policy,
            "learning_score": score
        }


        self.history.append(
            record
        )


        return record


    def get_history(self):

        return self.history