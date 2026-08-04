from .portfolio_runtime_service import PortfolioRuntimeService


class PortfolioRuntimeFacade:


    def __init__(self):

        self.service = PortfolioRuntimeService()



    def execute(
        self,
        event
    ):

        return self.service.run(
            event
        )