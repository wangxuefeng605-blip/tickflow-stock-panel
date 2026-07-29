class WeightProvider:


    def __init__(self):

        self.weights = {

            "momentum":0.2,

            "trend":0.3,

            "volatility":0.1,

            "liquidity":0.2,

            "value":0.2

        }



    def get_weights(self):

        return self.weights.copy()



    def update(
        self,
        weights
    ):

        self.weights.update(
            weights
        )