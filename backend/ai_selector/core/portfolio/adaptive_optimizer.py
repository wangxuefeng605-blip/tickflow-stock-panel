class PortfolioAdaptiveOptimizer:


    def optimize(
        self,
        outcome
    ):

        reward = outcome.get(
            "return",
            0
        )

        risk = outcome.get(
            "max_drawdown",
            0
        )


        return {

            "portfolio_weight":
                1 + reward - risk,

            "risk_adjustment":
                1 - risk

        }