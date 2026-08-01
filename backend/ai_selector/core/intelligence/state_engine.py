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


        # normalize trend

        if isinstance(trend, str):

            trend_map = {

                "UP": 0.8,

                "DOWN": 0.2,

                "SIDEWAY": 0.5

            }

            trend = trend_map.get(
                trend.upper(),
                0.5
            )


        else:

            trend = float(trend)



        # normalize volatility

        if isinstance(volatility, str):

            volatility_map = {

                "HIGH": 0.8,

                "LOW": 0.2,

                "MEDIUM":0.5

            }

            volatility = volatility_map.get(
                volatility.upper(),
                0.5
            )

        else:

            volatility=float(volatility)



        if trend >= 0.6:

            if volatility < 0.4:

                return "BULL"

            return "BEAR"


        return "SIDEWAY"