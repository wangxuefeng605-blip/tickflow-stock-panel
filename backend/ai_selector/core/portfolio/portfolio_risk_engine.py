"""
Portfolio Risk Engine

Stage32 Portfolio Intelligence Layer
"""


class PortfolioRiskEngine:


    def evaluate(
        self,
        portfolio
    ):

        exposure = portfolio.exposure()


        risk = "LOW"


        if exposure > 0.8:

            risk = "HIGH"

        elif exposure > 0.5:

            risk = "MEDIUM"



        return {

            "exposure": exposure,

            "risk": risk
        }