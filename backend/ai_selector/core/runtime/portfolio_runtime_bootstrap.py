from .portfolio_runtime_executor import PortfolioRuntimeExecutor


class PortfolioRuntimeBootstrap:

    def __init__(self):
        self.executor = PortfolioRuntimeExecutor()

    def start(self, event):
        return self.execute(event)

    def execute(self, event):
        return self.executor.execute(event)

    def process(self, event):
        return self.execute(event)