class StrategyEvolver:

    def evolve(
        self,
        market,
        feedback
    ):

        reward = feedback.get(
            "reward",
            0
        )

        if market == "BULL":

            return {
                "momentum": 0.4 + reward * 0.1,
                "quality": 0.3,
                "value": 0.2,
                "risk": 0.1
            }

        if market == "BEAR":

            return {
                "momentum":0.1,
                "quality":0.3,
                "value":0.2,
                "risk":0.4
            }

        return {
            "momentum":0.25,
            "quality":0.25,
            "value":0.25,
            "risk":0.25
        }