from .learning_pipeline import LearningPipeline
from .learning_runtime_bridge import LearningRuntimeBridge
from .prediction_lifecycle import PredictionLifecycle



class LearningRuntimeOrchestrator:


    def __init__(self):

        self.pipeline = LearningPipeline()

        self.bridge = LearningRuntimeBridge()

        self.lifecycle = PredictionLifecycle()



    def after_scan(
        self,
        results
    ):

        return self.pipeline.process_scan(
            results
        )



    def after_rank(
        self,
        ranking
    ):

        return self.pipeline.process_rank(
            ranking
        )



    def record_prediction(
        self,
        results,
        date
    ):

        return self.lifecycle.record_top10(
            results,
            date
        )


    def process_feedback(
        self,
        feedbacks,
        weights
    ):

        return self.pipeline.process_feedback(
            feedbacks,
            weights
        )


    def feedback(
        self,
        factor,
        entry,
        future
    ):

        return self.bridge.process_feedback(
            factor,
            entry,
            future
        )



class LearningOrchestrator(
    LearningRuntimeOrchestrator
):
    pass