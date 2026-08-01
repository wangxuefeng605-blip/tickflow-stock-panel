from .learning_pipeline import LearningPipeline
from .learning_runtime_bridge import LearningRuntimeBridge


class LearningRuntimeOrchestrator:


    def __init__(self):

        self.pipeline = LearningPipeline()

        self.bridge = LearningRuntimeBridge()



    def after_scan(
        self,
        results
    ):

        if hasattr(
            self.pipeline,
            "process_scan"
        ):

            return self.pipeline.process_scan(
                results
            )

        return results



    def after_rank(
        self,
        results
    ):

        if hasattr(
            self.pipeline,
            "process_rank"
        ):

            return self.pipeline.process_rank(
                results
            )

        return results



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