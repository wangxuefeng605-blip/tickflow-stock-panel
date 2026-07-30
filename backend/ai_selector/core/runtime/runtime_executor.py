from core.runtime.contract import (
    RuntimeRequest,
    RuntimeResponse,
)

from core.runtime.runtime_pipeline import RuntimePipeline


class RuntimeExecutor:


    def __init__(self):

        self.pipeline = RuntimePipeline()


    def execute(
        self,
        stock
    ):

        request = RuntimeRequest(
            stock["code"],
            stock
        )


        result = self.pipeline.execute(
             stock
        )

        response = RuntimeResponse(
            request.code,
            result
        )


        return {
            **response.result,
            "executor_completed": True
        }