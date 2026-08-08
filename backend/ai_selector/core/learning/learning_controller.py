"""
Learning Controller

Stage35 Autonomous Learning
"""


class LearningController:


    def __init__(
        self,
        collector,
        evaluator,
        state
    ):

        self.collector = collector
        self.evaluator = evaluator
        self.state = state



    def learn(
        self,
        experience
    ):

        collected = self.collector.collect(
            experience
        )


        evaluation = self.evaluator.evaluate(
            experience
        )


        self.state.update_reward(
            evaluation["reward"]
        )


        return {
            "status": "LEARNED",
            "evaluation": evaluation,
            "state": self.state.snapshot()
        }