class LearningRuntimeOrchestrator:


    def __init__(self):

        self.pipeline = LearningPipeline()

        self.bridge = LearningRuntimeBridge()


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