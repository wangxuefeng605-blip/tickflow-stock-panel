from core.scanner.learning_runtime_adapter import ScannerLearningRuntimeAdapter


class AISelectorRuntime:

    def __init__(self):
        self.learning = ScannerLearningRuntimeAdapter()


    def run(
        self,
        stock
    ):

        result = self.learning.process(
            stock
        )

        return {
            **result,
            "runtime_completed": True
        }