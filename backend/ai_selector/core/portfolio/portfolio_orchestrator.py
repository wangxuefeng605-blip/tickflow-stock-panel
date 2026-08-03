from .intelligence_runtime import PortfolioIntelligenceRuntime


class PortfolioOrchestrator:


    def __init__(self):

        self.runtime = PortfolioIntelligenceRuntime()


    def run(self, market, signals):

        return self.runtime.execute(
            market,
            signals
        )