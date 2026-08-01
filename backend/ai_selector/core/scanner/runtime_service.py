from .runtime_executor import RuntimeExecutor


class RuntimeService:

    def __init__(self):
        self.executor = RuntimeExecutor()


    def execute(self, payload):

        result = self.executor.execute(
            payload
        )

        result["runtime_service_completed"] = True

        return result


    def run(self):

        return {
            "status": "running"
        }


ScannerRuntimeService = RuntimeService