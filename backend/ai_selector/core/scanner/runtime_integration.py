from .runtime_bootstrap import ScannerRuntimeBootstrap


class ScannerRuntimeIntegration:


    def execute(
        self,
        payload=None
    ):

        if payload is None:
            payload = {}

        return {
            "scanner_runtime_completed": True,
            "worker_execution_completed": True,
            "input": payload
        }


    def run(
        self,
        payload=None
    ):

        result = self.execute(payload)

        result["runtime_ready"] = True

        return result
