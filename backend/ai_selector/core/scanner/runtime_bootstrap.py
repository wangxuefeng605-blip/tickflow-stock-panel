from .runtime_facade import ScannerRuntimeFacade


class ScannerRuntimeBootstrap:

    def __init__(self):
        self.facade = ScannerRuntimeFacade()

    def start(self):
        return self.facade.status()