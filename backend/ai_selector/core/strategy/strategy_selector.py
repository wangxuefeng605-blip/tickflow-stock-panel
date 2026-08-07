class StrategySelector:

    def select(self, context):

        market = context.get("market")

        if market == "bull":
            return "trend_follow"

        if market == "bear":
            return "defensive"

        return "neutral"