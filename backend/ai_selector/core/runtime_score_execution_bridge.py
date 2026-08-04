class RuntimeScoreExecutionBridge:


    def __init__(self):

        self.weights = None


    def bind(self, weights):

        self.weights = weights

        return {
            "connected": True,
            "weights": weights
        }


    def execute(self, score):

        if not self.weights:

            return score


        factor = self.weights.get(
            "momentum",
            1.0
        )

        return score * factor