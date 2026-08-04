class PortfolioRuntimeService:

    def __init__(self):
        self.bridge = PortfolioRuntimeBridge()


    def run(
        self,
        event
    ):
        return self.bridge.process(event)