"""
Learning Feedback Processor

Stage29 Meta Learning Engine
"""


from .meta_weight_optimizer import (
    MetaWeightOptimizer
)


class LearningFeedbackProcessor:


    def __init__(self):

        self.optimizer = MetaWeightOptimizer()


    def process(
        self,
        feedback,
        weights
    ):

        return self.optimizer.update(
            weights,
            feedback
        )