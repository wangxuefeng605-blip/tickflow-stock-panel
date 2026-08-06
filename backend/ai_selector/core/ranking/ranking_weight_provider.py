from core.learning.weight_provider import LearningWeightProvider


class RankingWeightProvider:


    def __init__(self):

        self.provider = LearningWeightProvider()


    def get_weight(
        self,
        factor
    ):

        return self.provider.get_weight(
            factor
        )