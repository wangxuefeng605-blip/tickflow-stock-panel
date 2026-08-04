from core.learning.runtime import LearningRuntime


class PortfolioLearningAdapter:


    def __init__(self):

        self.learning = LearningRuntime()


    def update(
        self,
        portfolio_feedback
    ):

        weights = {
            "momentum":0.35,
            "trend":0.30,
            "quality":0.15,
            "liquidity":0.10,
            "risk":0.10
        }


        return self.learning.process(
            portfolio_feedback,
            weights
        )