class WeightProvider:


    DEFAULT_WEIGHTS = {
        "momentum": 0.2
    }


    def __init__(self, weights=None):

        self.weights = (
            weights.copy()
            if weights
            else self.DEFAULT_WEIGHTS.copy()
        )


    def get_weight(self, factor):

        return self.weights.get(
            factor,
            1.0
        )


    def get_weights(self):

        return self.weights.copy()


    def update(self, weights):

        self.weights.update(
            weights
        )



def inject_weights(base_weights, learned_weights):

    result = base_weights.copy()

    result.update(
        learned_weights
    )

    return result



def inject_learning_weight(weights, learning_result):

    return inject_weights(
        weights,
        learning_result
    )



LearningWeightProvider = WeightProvider