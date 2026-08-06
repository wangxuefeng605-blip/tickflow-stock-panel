"""
Daily Feedback Runner

Load previous portfolio feedback
and update ranking weights.
"""


from core.learning.feedback_engine import (
    FeedbackLearningEngine
)


class DailyFeedbackRunner:


    def __init__(self):

        self.engine = (
            FeedbackLearningEngine()
        )


    def update(
        self,
        weights,
        feedbacks
    ):

        result = (
            self.engine.update_weights(
                weights,
                feedbacks
            )
        )

        return result["weights"]