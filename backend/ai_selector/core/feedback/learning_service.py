"""
Feedback Learning Service

Stage54 Step6
"""

from .storage import FeedbackStorage
from .evaluator import FeedbackEvaluator
from .weight_updater import FeedbackWeightUpdater


class FeedbackLearningService:


    def __init__(
        self,
        storage=None,
        evaluator=None,
        updater=None
    ):

        self.storage = (
            storage
            or FeedbackStorage()
        )

        self.evaluator = (
            evaluator
            or FeedbackEvaluator()
        )

        self.updater = (
            updater
            or FeedbackWeightUpdater()
        )


    def learn(self, weights):

        records = self.storage.load()


        result = self.evaluator.evaluate(
            records
        )


        score = result.get(
            "accuracy",
            0.5
        )


        return self.updater.update(
            weights,
            score
        )