from core.learning.runtime import LearningRuntime


class PortfolioLearningAdapter:


    def __init__(self):

        self.learning = LearningRuntime()



    def update(
        self,
        portfolio_feedback
    ):

        return self.learning.process(
            portfolio_feedback
        )