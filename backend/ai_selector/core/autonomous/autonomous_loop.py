from core.learning.performance_evaluator import (
    PerformanceEvaluator
)

from core.learning.learning_loop import (
    LearningLoop
)

from core.optimization.optimization_loop import (
    OptimizationLoop
)


class AutonomousLoop:

    def __init__(self):

        self.evaluator = PerformanceEvaluator()

        self.learning = LearningLoop()

        self.optimizer = OptimizationLoop()


    def _normalize_feedback(self, context):

        if isinstance(context, dict):

            return [
                {
                    "code": context.get(
                        "strategy",
                        "unknown"
                    ),
                    "score": context.get(
                        "score",
                        0
                    ),
                    "return": context.get(
                        "return",
                        0
                    )
                }
            ]

        return context


    def run(self, context):

        feedbacks = self._normalize_feedback(
            context
        )


        performance = self.evaluator.evaluate(
            feedbacks
        )


        if hasattr(
            self.learning,
            "run"
        ):

            learning_result = self.learning.run(
                performance
            )

        elif hasattr(
            self.learning,
            "execute"
        ):

            learning_result = self.learning.execute(
                performance
            )

        elif hasattr(
            self.learning,
            "process"
        ):

            learning_result = self.learning.process(
                performance
            )

        else:

            learning_result = performance


        if hasattr(
            self.optimizer,
            "run"
        ):

            optimized = self.optimizer.run(
                learning_result
            )

        else:

            optimized = learning_result


        return {
            "status": "improved",
            "strategy": optimized
        }