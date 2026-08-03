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


    def apply_adjustment(
        self,
        adjustments
    ):

        for factor, delta in adjustments.items():

            current = self.weights.get(
                factor,
                0
            )


            new_value = (
                current
                +
                delta
            )


            # clamp
            new_value = max(
                0,
                min(
                    1,
                    new_value
                )
            )


            self.weights[factor] = (
                new_value
            )


        self._normalize()


        return self.weights.copy()



    def _normalize(
        self
    ):

        total = sum(
            self.weights.values()
        )


        if total <= 0:
            return


        for key in self.weights:

            self.weights[key] = (
                self.weights[key]
                /
                total
            )



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