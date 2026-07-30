from .persistence import LearningPersistence
class LearningEngine:

    def __init__(
        self,
        optimizer,
        provider
    ):
        self.optimizer = optimizer
        self.provider = provider


    def learn(
        self,
        weights,
        feedback
    ):

        updated = self.optimizer.update(
            weights,
            feedback
        )

        self.provider.update(
            updated
        )

        return updated