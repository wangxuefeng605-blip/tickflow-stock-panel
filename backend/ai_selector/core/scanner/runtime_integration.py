from .runtime_bootstrap import ScannerRuntimeBootstrap


class ScannerRuntimeIntegration:


    def __init__(self):

        self.bootstrap = ScannerRuntimeBootstrap()


    def execute(self, payload):

        result = self.bootstrap.execute(payload)

        result["runtime_integration_completed"] = True

        return result