from core.runtime.portfolio_runtime_facade import PortfolioRuntimeFacade


class PortfolioRuntimeExecutor:

    def __init__(self):
        self.facade = PortfolioRuntimeFacade()


    def execute(self, command):

        return self.facade.execute(
            command
        )