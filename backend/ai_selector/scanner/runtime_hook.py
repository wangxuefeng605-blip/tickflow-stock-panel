from .runtime_integration import ScannerRuntimeIntegration


class ScannerRuntimeHook:

    def __init__(self):
        self.runtime = None


    def execute(self, stock):

        if self.runtime is None:
            from .runtime_integration import ScannerRuntimeIntegration
            self.runtime = ScannerRuntimeIntegration()

        result = self.runtime.execute(stock)

        result["scanner_runtime_hook_completed"] = True
        result["runtime_hook_completed"] = True

        return result