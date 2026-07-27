class MarketStateEngine:


    def detect(
        self,
        market
    ):

        trend = market.get(
            "trend",
            0
        )

        volatility = market.get(
            "volatility",
            0
        )


        if (
            trend >= 0.6
            and
            volatility < 0.4
        ):
            return "BULL"



        if trend <= 0.3:

            return "BEAR"



        return "SIDEWAY"