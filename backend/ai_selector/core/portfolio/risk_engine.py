class PortfolioRiskEngine:


    def check(
        self,
        allocation
    ):

        if allocation <= 0.8:
            return True

        return False