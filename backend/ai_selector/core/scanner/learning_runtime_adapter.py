from core.learning.pipeline_assembly import LearningPipelineAssembly


class ScannerLearningRuntimeAdapter:


    def __init__(self):

        self.pipeline = LearningPipelineAssembly()


    def process(
        self,
        scanner_result,
        learning_state=None
    ):

        return self.pipeline.execute(
            scanner_result
        )


    def run(
        self,
        scanner_result
    ):

        return self.process(
            scanner_result
        )