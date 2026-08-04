from core.portfolio.feedback_loop import PortfolioFeedbackLoop
from core.learning.portfolio_adapter import PortfolioLearningAdapter


class PortfolioFeedbackRuntime:


    def __init__(self):

        self.feedback = PortfolioFeedbackLoop()

        self.adapter = PortfolioLearningAdapter()


    def run(
        self,
        performance
    ):

        result = self.feedback.analyze(
            performance
        )


        return self.adapter.update(
            result
        )