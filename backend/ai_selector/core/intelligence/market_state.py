class MarketState:


    def detect(
        self,
        market_data=None
    ):

        if not market_data:
            return "UNKNOWN"


        trend = market_data.get(
            "trend",
            0
        )


        if trend > 0:
            return "BULL"


        if trend < 0:
            return "BEAR"


        return "SIDEWAYS"