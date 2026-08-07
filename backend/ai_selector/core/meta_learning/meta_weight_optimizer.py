"""
Meta Weight Optimizer

Stage29 Meta Learning Engine
"""


class MetaWeightOptimizer:


    def update(
        self,
        weights,
        feedback
    ):

        new_weights = weights.copy()


        factor = feedback.get(
            "factor"
        )

        reward = feedback.get(
            "reward",
            0
        )


        if factor in new_weights:

            if reward > 0:

                new_weights[factor] += 0.05

            else:

                new_weights[factor] -= 0.05


        return new_weights