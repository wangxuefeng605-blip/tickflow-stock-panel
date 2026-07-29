from copy import deepcopy


class WeightOptimizer:


    def update(
        self,
        weights,
        feedback
    ):

        new_weights = deepcopy(
            weights
        )


        factor = (
            1 + feedback.adjustment
        )


        for key in new_weights:

            new_weights[key] = round(
                new_weights[key] * factor,
                6
            )


        return new_weights