class MarketAgent:

    def run(self, context):

        market = context.get(
            "market",
            "UNKNOWN"
        )

        if market == "BULL":
            signal = "positive"

        elif market == "BEAR":
            signal = "negative"

        else:
            signal = "neutral"

        return {
            "agent": "market",
            "market": market,
            "signal": signal
        }