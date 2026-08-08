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


class FeedbackEngine:

    def evaluate(self, result):
        """
        Evaluate single strategy feedback.

        Compatibility interface for AutonomousLearner.
        """

        if not result:
            return {
                "score": 0,
                "reward": 0,
                "success": False
            }

        score = result.get(
            "score",
            0
        )

        ret = result.get(
            "return",
            0
        )

        return {
            "strategy": result.get(
                "strategy"
            ),

            "score": score,

            "return": ret,

            "reward": ret,

            "success": score >= 0.8
        }
 
    
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
class FeedbackLearningEngine(FeedbackEngine):
    """
    Backward compatible learning feedback engine.
    """

    pass