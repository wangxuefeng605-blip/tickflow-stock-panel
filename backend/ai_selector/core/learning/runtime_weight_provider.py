class RuntimeWeightProvider:

    def __init__(self):

        self.weights = {

            "momentum": 0.35,
            "trend": 0.30,
            "volume_factor": 0.15,
            "quality": 0.10,
            "growth": 0.05,
            "volatility": 0.05,

        }

    def get_weights(
        self
    ):

        return self.weights.copy()

    def get_weight(
        self,
        factor
    ):

        return self.weights.get(
            factor,
            0.0
        )

    def update(
        self,
        weights
    ):

        if not isinstance(
            weights,
            dict
        ):
            return self.get_weights()

        self.weights.update(
            weights
        )

        return self.get_weights()

    def update_weights(
        self,
        weights
    ):

        return self.update(
            weights
        )