class StrategySelector:


    def select(
        self,
        context
    ):


        if context.state=="BULL":

            return "momentum"


        if context.state=="BEAR":

            return "defensive"


        return "neutral"