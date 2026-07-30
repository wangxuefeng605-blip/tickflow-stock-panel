from .runtime_service import ScannerRuntimeService


class ScannerRuntimeFacade:

    def __init__(self):
        self.service = ScannerRuntimeService()

    def run(self):
        return self.service.run()

    def status(self):
        return {
            "status": "ready"
        }