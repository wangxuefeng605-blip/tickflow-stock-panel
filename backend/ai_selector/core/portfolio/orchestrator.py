from .intelligence import PortfolioIntelligence
from .intelligence_runtime import PortfolioIntelligenceRuntime


class PortfolioOrchestrator:


    def __init__(self):

        self.intelligence = PortfolioIntelligence()
        self.runtime = PortfolioIntelligenceRuntime()



    def analyze(
        self,
        data
    ):

        performance = data.get(
            "performance",
            {}
        )

        risk = data.get(
            "risk",
            {}
        )

        attribution = data.get(
            "attribution",
            []
        )


        result = self.intelligence.analyze(
            performance,
            risk,
            attribution
        )


        # backward compatibility
        if "risk" not in result:

            result["risk"] = result.get(
                "risk_level",
                "UNKNOWN"
            )


        # backward compatibility
        if "intelligence" not in result:

            result["intelligence"] = {
                "portfolio_score": result.get(
                    "portfolio_score",
                    0
                ),
                "risk": result.get(
                    "risk",
                    "UNKNOWN"
                ),
                "drivers": result.get(
                    "top_drivers",
                    []
                )
            }


        return result


       



    def run(
        self,
        market,
        signals
    ):

        return self.runtime.execute(
            market,
            signals
        )