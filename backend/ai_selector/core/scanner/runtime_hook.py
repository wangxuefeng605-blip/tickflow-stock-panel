from core.scanner.runtime_integration import ScannerRuntimeIntegration


class ScannerRuntimeHook:


    def __init__(self):

        self.runtime = ScannerRuntimeIntegration()



    def execute(
        self,
        stock
    ):

        result = self.runtime.execute(
            stock
        )

        return {
            **result,
            "runtime_hook_completed": True
        }