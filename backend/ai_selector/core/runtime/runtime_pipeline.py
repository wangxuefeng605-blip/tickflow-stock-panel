from core.runtime.ai_selector_runtime import AISelectorRuntime


class RuntimePipeline:

    def __init__(self):

        self.runtime = AISelectorRuntime()


    def execute(
        self,
        stock
    ):

        result = self.runtime.run(
            stock
        )

        return {
            **result,
            "pipeline_runtime_completed": True
        }