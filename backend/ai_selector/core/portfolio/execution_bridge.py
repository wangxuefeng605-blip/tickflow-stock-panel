class ExecutionPortfolioBridge:


    def __init__(
        self,
        portfolio
    ):
        self.portfolio = portfolio


    def process(
        self,
        order
    ):

        if order["action"] == "BUY":

            self.portfolio.buy(
                order["code"],
                order["price"],
                order["qty"]
            )


        return {

            "cash":
                self.portfolio.cash,

            "positions":
                self.portfolio.positions

        }