"""
Feedback Learning Engine

Combine portfolio feedback
and generate updated ranking weights.
"""


from core.learning.performance_evaluator import (
    PerformanceEvaluator
)

from core.learning.learning_signal import (
    LearningSignalGenerator
)

from core.learning.weight_adapter import (
    WeightAdapter
)


class FeedbackLearningEngine:


    def __init__(self):

        self.evaluator = PerformanceEvaluator()

        self.signal_generator = (
            LearningSignalGenerator()
        )

        self.adapter = WeightAdapter()



    def update_weights(
        self,
        weights,
        feedbacks
    ):

        performance = (
            self.evaluator.evaluate(
                feedbacks
            )
        )


        learning = (
            self.signal_generator.generate(
                performance
            )
        )


        new_weights = (
            self.adapter.apply(
                weights,
                learning["signals"]
            )
        )


        return {
            "weights": new_weights,
            "performance": performance,
            "learning": learning
        }