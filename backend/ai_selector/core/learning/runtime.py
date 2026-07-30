from .optimizer import LearningOptimizer


class LearningRuntime:

    def __init__(self):
        self.weights = {
            "momentum": 1.0
        }


    def learn(self, feedback):

        factor = feedback.get(
            "factor"
        )

        reward = feedback.get(
            "reward",
            0
        )

        if factor:
            self.weights[factor] = (
                self.weights.get(
                    factor,
                    1
                )
                + reward
            )

        return self.weights