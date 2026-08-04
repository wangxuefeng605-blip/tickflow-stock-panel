class PortfolioFeedback:


    def evaluate(
        self,
        outcome
    ):

        profit = outcome.get(
            "profit",
            0
        )

        return {

            "reward": profit,

            "source":
                "portfolio"

        }



    def process(
        self,
        feedback
    ):

        reward = feedback.get(
            "reward",
            0
        )

        performance = feedback.get(
            "performance",
            {}
        )


        return {

            "reward":
                reward,

            "performance":
                performance,

            "source":
                "portfolio_feedback"

        }