class PortfolioRiskEngine:


    def check(
        self,
        allocation
    ):

        if allocation <= 1.0:
            return True

        return False