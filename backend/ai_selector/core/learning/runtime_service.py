from .learning_orchestrator import (
    LearningOrchestrator
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