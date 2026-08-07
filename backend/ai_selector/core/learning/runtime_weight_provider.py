class RuntimeWeightProvider:


    def __init__(self):

        self.weights = {

            "momentum":0.35,

            "trend":0.30,

            "quality":0.15,

            "liquidity":0.10,

            "risk":0.10

        }


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

        return self.get_weights()