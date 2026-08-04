class PortfolioLearningBridge:

    def __init__(self):
        pass


    def evaluate(
        self,
        portfolio_result
    ):

        reward = 0


        if portfolio_result.get(
            "return",
            0
        ) > 0:

            reward = 1


        elif portfolio_result.get(
            "return",
            0
        ) < 0:

            reward = -1


        return {
            "reward": reward,
            "source": "portfolio"
        }