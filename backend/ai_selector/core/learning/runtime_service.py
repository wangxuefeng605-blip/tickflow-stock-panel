from .learning_orchestrator import (
    LearningOrchestrator
)
from .runtime_weight_provider import (
    RuntimeWeightProvider
)



class LearningRuntimeService:


    def __init__(self):

        self.orchestrator = (
            LearningOrchestrator()
        )


    def record_prediction(
        self,
        top10,
        date
    ):

        return (
            self.orchestrator.record_prediction(
                top10,
                date
            )
        )


    def process_daily(
        self,
        top10,
        date
    ):

        return self.record_prediction(
            top10,
            date
        )

    def update_weights(
        self,
        weights
    ):

        return self.weight_provider.update(
            weights
        )


    def get_weights(
        self
    ):

        return self.weight_provider.get_weights()