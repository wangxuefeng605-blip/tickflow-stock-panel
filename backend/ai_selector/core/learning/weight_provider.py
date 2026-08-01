class WeightProvider:


    def __init__(
        self,
        weights=None
    ):

        self.weights = weights or {
            "momentum": 0.2,
            "trend": 0.2,
            "value": 0.2,
            "quality": 0.2
        }


    def get_weight(
        self,
        factor
    ):

        return self.weights.get(
            factor,
            1.0
        )


    def get_weights(
        self
    ):

        return self.weights.copy()


    def update(
        self,
        weights
    ):

        self.weights.update(
            weights
        )

        return self.weights



class LearningWeightProvider(
    WeightProvider
):

    pass



def inject_weights(
    base,
    learned
):

    result = base.copy()

    result.update(
        learned
    )

    return result



def inject_learning_weight(
    base,
    learned
):

    return inject_weights(
        base,
        learned
    )