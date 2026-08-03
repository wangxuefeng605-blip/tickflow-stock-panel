class PortfolioPerformance:

    def __init__(self, portfolio):
        self.portfolio = portfolio


    def evaluate(self):

        return {
            "return": self.calculate_return(),
            "drawdown": self.calculate_drawdown(),
            "score": self.calculate_score()
        }


    def calculate_return(self):

        return 0


    def calculate_drawdown(self):

        return 0


    def calculate_score(self):

        return (
            self.calculate_return() * 0.5
            - self.calculate_drawdown() * 0.3
        )