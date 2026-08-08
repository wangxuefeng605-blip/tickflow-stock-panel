"""
Adaptive Controller

Stage36 Adaptive Intelligence
"""


class AdaptiveController:


    def __init__(
        self,
        state,
        evaluator
    ):

        self.state = state
        self.evaluator = evaluator



    def adapt(
        self,
        performance
    ):


        evaluation = self.evaluator.evaluate(
            performance
        )


        self.state.update_performance(
            performance
        )


        if evaluation["should_adjust"]:

            self.state.adjust_strategy()


        return {

            "status": "ADAPTED",

            "evaluation":
                evaluation,

            "state":
                self.state.snapshot()
        }