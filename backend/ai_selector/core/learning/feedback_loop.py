from core.backtest.learning import (
    BacktestLearningEngine
)

from core.learning.feedback import (
    FeedbackEngine
)

from core.learning.weight_optimizer import (
    WeightOptimizer
)



class FeedbackLoop:


    def __init__(self):

        self.learning = BacktestLearningEngine()

        self.feedback = FeedbackEngine()

        self.optimizer = WeightOptimizer()



    def run(
        self,
        result,
        weights
    ):

        signal = self.learning.analyze(
            result
        )


        event = self.feedback.generate(
            signal
        )


        updated = self.optimizer.update(
            weights,
            event
        )


        return updated