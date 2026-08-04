from .portfolio_runtime_bridge import PortfolioRuntimeBridge



class PortfolioRuntimeService:


    def __init__(self):

        self.bridge = PortfolioRuntimeBridge()



    def run(
        self,
        event
    ):

        return self.bridge.execute(
            event
        )