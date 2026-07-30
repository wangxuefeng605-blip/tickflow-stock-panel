class LearningScannerAdapter:


    def __init__(
        self,
        weight_provider
    ):
        self.weight_provider = weight_provider


    def get_factor_weight(
        self,
        factor
    ):

        return self.weight_provider.get_weight(
            factor
        )