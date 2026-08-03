class PortfolioLearningBridge:


    def __init__(self):

        self.optimizer = LearningOptimizer()



    def learn(
        self,
        portfolio_feedback
    ):

        return self.optimizer.update(
            portfolio_feedback
        )