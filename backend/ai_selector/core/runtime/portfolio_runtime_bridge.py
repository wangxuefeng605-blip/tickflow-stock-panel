from core.portfolio.intelligence_runtime import PortfolioIntelligenceRuntime


class PortfolioRuntimeBridge:


    def __init__(self):

        self.intelligence = PortfolioIntelligenceRuntime()


    def process(
        self,
        event
    ):

        return self.intelligence.run(
            event
        )