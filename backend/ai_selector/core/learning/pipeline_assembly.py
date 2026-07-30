from .runtime_orchestrator import LearningRuntimeOrchestrator


class LearningPipelineAssembly:


    def __init__(self):

        self.runtime = LearningRuntimeOrchestrator()



    def execute(
        self,
        stock
    ):

        result = self.runtime.run(
            stock
        )


        return {
            **result,
            "pipeline_completed": True
        }