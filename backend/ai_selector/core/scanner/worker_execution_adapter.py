from core.scanner.worker_runtime import WorkerRuntimeInjection


class WorkerExecutionAdapter:


    def __init__(self):

        self.runtime = WorkerRuntimeInjection()



    def execute(
        self,
        stock
    ):

        result = self.runtime.execute(
            stock
        )

        return {
            **result,
            "worker_execution_completed": True
        }