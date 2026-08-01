from core.scanner.worker_execution_pipeline import WorkerExecutionPipeline


class RuntimeExecutor:


    def __init__(self):

        self.pipeline = WorkerExecutionPipeline()



    def execute(self, task):

        result = self.pipeline.execute(
            task
        )

        return {
            **result,
            "runtime_completed": True
        }