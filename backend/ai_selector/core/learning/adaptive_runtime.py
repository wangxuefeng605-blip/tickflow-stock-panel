from core.learning.feedback_analyzer import (
    FeedbackAnalyzer
)

from core.learning.weight_adjuster import (
    WeightAdjuster
)


class AdaptiveRuntime:


    def __init__(self):

        self.feedback_analyzer = (
            FeedbackAnalyzer()
        )

        self.weight_adjuster = (
            WeightAdjuster()
        )



    def update_weights(self):

        feedback = (
            self.feedback_analyzer.analyze()
        )


        adjustments = (
            self.weight_adjuster.adjust(
                feedback
            )
        )


        return adjustments