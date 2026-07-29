class StrategySelector:


    def select(
        self,
        state
    ):

        if state == "BULL":
            return "momentum"

        if state == "BEAR":
            return "defensive"

        return "balanced"