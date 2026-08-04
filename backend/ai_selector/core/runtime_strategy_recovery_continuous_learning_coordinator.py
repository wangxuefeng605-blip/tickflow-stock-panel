class RuntimeStrategyRecoveryContinuousLearningCoordinator:
    """
    Coordinate continuous recovery strategy learning.
    """

    def __init__(self):

        self.history = []


    def coordinate(self, feedback):

        signal = feedback.get(
            "learning_signal",
            0
        )

        quality = feedback.get(
            "recovery_quality",
            "unknown"
        )


        if signal > 0:

            learning_action = "reinforce"

        elif signal < 0:

            learning_action = "adjust"

        else:

            learning_action = "observe"


        result = {
            "learning_action": learning_action,
            "signal": signal,
            "quality": quality
        }


        self.history.append(
            result
        )


        return result


    def get_history(self):

        return self.history