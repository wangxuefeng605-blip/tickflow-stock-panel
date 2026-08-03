class AutonomousPortfolioEngine:


    def __init__(
        self,
        strategy,
        allocator,
        risk
    ):

        self.strategy = strategy
        self.allocator = allocator
        self.risk = risk



    def decide(
        self,
        market,
        signal
    ):


        strategy = self.strategy.evolve(
            market,
            signal
        )


        allocation = self.allocator.allocate(
            strategy
        )


        risk_ok = self.risk.check(
            allocation
        )


        if risk_ok:

            return {

                "action":"BUY",

                "allocation":allocation,

                "confidence":
                    strategy.get(
                        "confidence",
                        0.5
                    )

            }


        return {

            "action":"HOLD",

            "allocation":0

        }
    