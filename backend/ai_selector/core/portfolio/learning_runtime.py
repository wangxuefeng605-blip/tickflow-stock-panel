class PortfolioLearningRuntime:


    def __init__(self):

        self.history = []


    def record(
        self,
        decision,
        outcome
    ):

        item = {
            "decision": decision,
            "outcome": outcome
        }

        self.history.append(
            item
        )

        return item


    def learn(
        self,
        outcome
    ):

        if outcome.get(
            "success",
            False
        ):

            return {
                "reward": 1,
                "signal": "POSITIVE"
            }


        return {
            "reward": -1,
            "signal": "NEGATIVE"
        }