class AdaptiveRankOptimizer:


    def __init__(self):

        self.learning_rate = 0.05



    def optimize(
        self,
        weights,
        feedbacks
    ):

        new_weights = dict(weights)


        if not feedbacks:
            return new_weights


        reward = sum(
            x.get(
                "reward",
                0
            )
            for x in feedbacks
        ) / len(feedbacks)


        if reward > 0.5:

            new_weights["momentum"] = (
                new_weights.get(
                    "momentum",
                    0
                )
                +
                self.learning_rate
            )


        else:

            new_weights["risk"] = (
                new_weights.get(
                    "risk",
                    0
                )
                +
                self.learning_rate
            )


        return new_weights