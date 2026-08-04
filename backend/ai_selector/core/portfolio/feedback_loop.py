class PortfolioFeedbackLoop:


    def analyze(
        self,
        performance
    ):

        ret = performance.get(
            "return",
            0
        )


        if ret > 0:
            reward = 1

        elif ret < 0:
            reward = -1

        else:
            reward = 0


        return {

            "reward": reward,

            "performance": performance,

            "source": "portfolio_feedback"

        }