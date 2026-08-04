class PortfolioRuntimeBridge:

    def __init__(self):
        self.intelligence = PortfolioIntelligenceRuntime()


    def process(
        self,
        portfolio_event
    ):

        return self.intelligence.run(
            portfolio_event
        )