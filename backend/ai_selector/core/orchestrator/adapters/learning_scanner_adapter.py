class LearningScannerAdapter:


    def __init__(self, provider):

        self.provider = provider



    def get_factor_weight(
        self,
        factor
    ):

        return self.provider.get_weight(
            factor
        )