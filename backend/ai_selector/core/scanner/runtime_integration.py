from core.scanner.runtime_bridge import RuntimeBridge


class ScannerRuntimeIntegration:


    def __init__(self):

        self.bridge = RuntimeBridge()



    def execute(
        self,
        stock
    ):

        result = self.bridge.execute(
            stock
        )

        return {
            **result,
            "scanner_runtime_completed": True
        }