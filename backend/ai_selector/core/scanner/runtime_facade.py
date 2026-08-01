from .runtime_service import ScannerRuntimeService


class ScannerRuntimeFacade:


    def __init__(self):

        self.service = ScannerRuntimeService()


    def execute(self, payload):

        return self.service.execute(payload)


    def status(self):

        return {
            "status": "ready"
        }