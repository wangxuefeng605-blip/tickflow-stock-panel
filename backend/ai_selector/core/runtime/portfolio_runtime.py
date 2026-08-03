class PortfolioRuntime:

    def __init__(
        self,
        portfolio,
        risk_engine
    ):
        self.portfolio = portfolio
        self.risk_engine = risk_engine


    def execute(self, order):

        if not self.risk_engine.check(order):
            return {
                "status":"REJECTED"
            }


        self.portfolio.apply(order)


        return {
            "status":"EXECUTED",
            "portfolio":self.portfolio.state()
        }