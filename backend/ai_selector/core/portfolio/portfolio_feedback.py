class PortfolioFeedback:


    def evaluate(
        self,
        outcome
    ):

        profit = outcome["profit"]


        return {

            "reward":
                profit,

            "source":
                "portfolio"

        }