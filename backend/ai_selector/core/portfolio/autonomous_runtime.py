from .intelligence import PortfolioIntelligence
from .optimizer import PortfolioOptimizer
from .risk_engine import PortfolioRiskEngine


class PortfolioAutonomousRuntime:


    def __init__(self):

        self.intelligence = PortfolioIntelligence()

        self.optimizer = PortfolioOptimizer()

        self.risk = PortfolioRiskEngine()



    def run(
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


        allocation = sum(
            p.get("weight", 0)
            for p in data.get(
                "positions",
                []
            )
        )

        risk = self.risk.check(
            allocation
        )


        allocation = self.optimizer.optimize(

            data,

            risk,

            data.get(
                "market_state",
                "UNKNOWN"
            )

        )


        return {

            "action":
                "HOLD",

            "risk":
                risk,

            "allocation":
                allocation,

            "intelligence":
                intelligence

        }