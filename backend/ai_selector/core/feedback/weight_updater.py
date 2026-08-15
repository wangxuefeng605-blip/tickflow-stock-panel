"""
Feedback Weight Updater

Stage54:
Learning Weight Update
"""


class FeedbackWeightUpdater:


    def __init__(
        self,
        learning_rate=0.05
    ):

        self.learning_rate = learning_rate



    def update(
        self,
        weights,
        feedback_score
    ):
        """
        根据反馈调整权重
        """

        factor = (
            feedback_score - 0.5
        )


        updated = {}


        for k, v in weights.items():

            updated[k] = (
                v
                *
                (
                    1
                    +
                    factor
                    *
                    self.learning_rate
                )
            )


        total = sum(
            updated.values()
        )


        if total > 0:

            updated = {
                k:
                value / total
                for k, value
                in updated.items()
            }


        return updated