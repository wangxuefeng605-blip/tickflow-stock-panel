from core.runtime.contract import (
    RuntimeRequest
)


class RuntimePipeline:


    def run(
        self,
        request
    ):

        return {
            "code": request.code,
            "result": request.features,
            "pipeline_completed": True
        }



    def execute(
        self,
        stock
    ):

        request = RuntimeRequest(
            stock["code"],
            stock
        )

        result = self.run(
            request
        )

        return {
            **result,
            "runtime_completed": True,
            "pipeline_runtime_completed": True
        }