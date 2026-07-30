from core.runtime.runtime_executor import RuntimeExecutor


class RuntimeService:


    def __init__(self):

        self.executor = RuntimeExecutor()



    def execute(
        self,
        stock
    ):

        result = self.executor.execute(
            stock
        )


        return {
            **result,
            "service_completed": True
        }