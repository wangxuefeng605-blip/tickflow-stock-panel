from .intelligence import PortfolioIntelligence
from .intelligence_runtime import PortfolioIntelligenceRuntime
from .optimizer import PortfolioOptimizer

class PortfolioOrchestrator:


    def __init__(self):

        self.intelligence = PortfolioIntelligence()

        self.optimizer = PortfolioOptimizer()



    def analyze(
        self,
        data
    ):


        intelligence = self.intelligence.analyze(

            data.get(
                "performance",
                {}
            ),

            data.get(
                "risk",
                {}
            ),

            data.get(
                "attribution",
                []
            )

        )


        optimization = self.optimizer.optimize(

            data,

            intelligence.get(
                "risk",
                {}
            ),

            data.get(
                "market_state",
                "UNKNOWN"
            )

        )


        intelligence["optimization"] = optimization


        return {
            **intelligence,

            # backward compatibility
            "intelligence": intelligence
        }


       



    def run(
        self,
        market,
        signals
    ):

        return self.runtime.execute(
            market,
            signals
        )