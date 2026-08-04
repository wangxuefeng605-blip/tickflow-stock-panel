from .portfolio_runtime_bootstrap import PortfolioRuntimeBootstrap


class PortfolioRuntimeAPI:
    """
    External API entry for portfolio runtime.
    """

    def __init__(self):
        self.runtime = PortfolioRuntimeBootstrap()

    def execute(self, event):
        return self.runtime.execute(event)

    def process(self, event):
        return self.runtime.process(event)