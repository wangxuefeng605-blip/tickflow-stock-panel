class FeedbackOptimizer:

    def __init__(
        self,
        optimizer,
        persistence
    ):
        self.optimizer = optimizer
        self.persistence = persistence


    def update(
        self,
        feedback
    ):

        weights = self.optimizer.optimize(
            feedback
        )

        self.persistence.save(
            weights
        )

        return weights