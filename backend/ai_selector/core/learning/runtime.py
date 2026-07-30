from core.learning.feedback_aggregator import (
    LearningFeedbackAggregator
)

from core.learning.adaptive_weight import (
    AdaptiveWeightEngine
)


class LearningRuntime:


    def __init__(self):

        self.weights = {
            "momentum":0.3
        }


    def learn(self, feedback):

        factor = feedback.get(
            "factor"
        )

        reward = feedback.get(
            "reward",
            0
        )


        if factor not in self.weights:
            self.weights[factor] = 1.0


        if reward > 0:

            self.weights[factor] += 1.0


        elif reward < 0:

            self.weights[factor] *= 0.5


        return {
            factor: self.weights[factor],
            "updated": True,
            "weights": self.weights
        }


    def process(
        self,
        feedback,
        weights
    ):


        updated_weights = dict(weights)


        signal = feedback.get(
            "signal",
            {}
        )


        changed=False


        for factor,value in signal.items():

            if factor not in updated_weights:
                continue


            if value < 0.1:

                updated_weights[factor] *= 0.5
                changed=True



        return {

            "updated": changed,

            "weights": updated_weights,

            "feedback": feedback
        }