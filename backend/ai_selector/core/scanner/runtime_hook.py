from core.scanner.worker import ScanWorker


class ScannerRuntimeHook:


    def execute(self, stock):

        code = stock["code"]


        worker = ScanWorker(
            code=code,
            context=stock.get("context")
        )


        result = worker.scan()


        if result is None:
            return {
                "code": code,
                "runtime_hook_completed": True,
                "scan_failed": True
            }


        return {
            **result,
            "hook_executed": True,
            "scanner_runtime_hook_completed": True,
            "runtime_hook_completed": True
        }