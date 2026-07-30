from core.scanner.runtime_hook import ScannerRuntimeHook


class WorkerRuntimeInjection:


    def __init__(self):

        self.runtime = ScannerRuntimeHook()



    def execute(
        self,
        stock
    ):

        result = self.runtime.execute(
            stock
        )

        return {
            **result,
            "worker_runtime_completed": True
        }