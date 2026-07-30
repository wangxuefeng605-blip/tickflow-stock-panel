class WeightProvider:

    def __init__(self):

        self.weights = {
            "momentum":0.2
        }


    def get_weight(self, name):

        return self.weights.get(
            name,
            0
        )


    def get_weights(self):

        return self.weights


    def update(self, weights):

        self.weights.update(
            weights
        )

        return self.weights