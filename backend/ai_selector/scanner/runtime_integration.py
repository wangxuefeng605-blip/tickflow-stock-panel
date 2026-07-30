from .runtime_bootstrap import ScannerRuntimeBootstrap


class ScannerRuntimeIntegration:

    def __init__(self):

        self.bootstrap = ScannerRuntimeBootstrap()


    def execute(self, payload):

        status = self.bootstrap.start()

        result = {}

        if isinstance(status, dict):
            result["runtime_ready"] = (
                status.get("status") == "ready"
            )
        else:
            result["runtime_ready"] = False

        result["status"] = status

        if isinstance(payload, dict):
            result.update(payload)

        result["runtime_integration_completed"] = True
        result["scanner_runtime_completed"] = True

        return result


    def run(self):

        result = self.execute(
            {
                "runtime": "scanner"
            }
        )

        result["scanner_runtime_integration_completed"] = True

        return result