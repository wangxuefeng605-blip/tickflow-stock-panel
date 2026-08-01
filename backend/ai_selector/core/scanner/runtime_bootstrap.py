from .runtime_facade import ScannerRuntimeFacade


class ScannerRuntimeBootstrap:


    def __init__(self):

        self.facade = ScannerRuntimeFacade()


    def execute(self, payload):

        return self.facade.execute(payload)


    def start(self):

        return self.facade.status()