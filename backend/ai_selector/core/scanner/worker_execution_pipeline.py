from core.scanner.worker_execution_adapter import WorkerExecutionAdapter


class WorkerExecutionPipeline:


    def __init__(self):

        self.adapter = WorkerExecutionAdapter()


    def execute(self, stock):

        result = self.adapter.execute(stock)

        return {
            **result,
            "worker_pipeline_completed": True
        }