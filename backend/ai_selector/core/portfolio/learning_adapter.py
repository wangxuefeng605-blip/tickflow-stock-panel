class PortfolioLearningAdapter:


    def __init__(
        self,
        learner
    ):

        self.learner = learner


    def update(
        self,
        feedback
    ):

        return self.learner.update(
            feedback
        )