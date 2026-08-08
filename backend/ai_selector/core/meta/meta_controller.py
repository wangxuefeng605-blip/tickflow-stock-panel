"""
Meta Controller

Coordinate meta learning workflow.
"""

from core.meta.meta_evaluator import MetaEvaluator
from core.meta.meta_optimizer import MetaOptimizer
from core.meta.meta_state import MetaState



class MetaController:


    def __init__(self):

        self.evaluator = MetaEvaluator()

        self.optimizer = MetaOptimizer()

        self.state = MetaState()



    def process(
        self,
        parameters,
        before,
        after
    ):


        evaluation = self.evaluator.evaluate(
            before,
            after
        )


        result = self.optimizer.optimize(
            parameters,
            evaluation["score"]
        )


        self.state.record_cycle(
            result["optimized"]
        )


        return {

            "evaluation":
                evaluation,

            "optimization":
                result,

            "state":
                self.state.snapshot()
        }