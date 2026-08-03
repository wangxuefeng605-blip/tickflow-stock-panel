from .risk import PortfolioRisk
from .intelligence import PortfolioIntelligence


class PortfolioOrchestrator:

    def __init__(self):
        self.risk = PortfolioRisk()
        self.intelligence = PortfolioIntelligence()


    def analyze(self, portfolio):

        risk_result = self.risk.evaluate(
            portfolio
        )


        intelligence_result = self.intelligence.analyze(

            portfolio.get(
                "performance",
                {}
            ),

            risk_result,

            portfolio.get(
                "attribution",
                []
            )
        )


        return {

            "risk": risk_result,

            "intelligence": intelligence_result
        }