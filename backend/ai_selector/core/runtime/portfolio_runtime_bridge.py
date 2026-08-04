from core.portfolio.intelligence_runtime import PortfolioIntelligenceRuntime



class PortfolioRuntimeBridge:


    def __init__(self):

        self.intelligence = PortfolioIntelligenceRuntime()



    def execute(
        self,
        event
    ):

        return self.intelligence.run(
            event
        )



    def process(
        self,
        event
    ):

        return self.execute(
            event
        )