class StockWeightProvider:


    def __init__(
        self,
        weights=None
    ):

        self.weights = weights or {}


    def get_weight(
        self,
        code
    ):

        return self.weights.get(
            code,
            1.0
        )


    def update(
        self,
        code,
        weight
    ):

        self.weights[code] = weight

        return weight


    def get_weights(
        self
    ):

        return self.weights.copy()