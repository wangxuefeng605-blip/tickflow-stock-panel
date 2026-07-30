class LearningRuntimeOrchestrator:


    def __init__(
        self,
        scanner=None
    ):

        self.scanner = scanner



    def run(
        self,
        stock
    ):

        if self.scanner:

            scanned = self.scanner.scan(
                stock
            )

        else:

            scanned = stock.copy()


        return {
            **scanned,
            "learning_applied": True,
            "decision": {
                "action": "hold"
            }
        }