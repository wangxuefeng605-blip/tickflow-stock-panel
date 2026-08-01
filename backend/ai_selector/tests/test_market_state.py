from core.intelligence.state_engine import MarketStateEngine



class MarketStateEngine:

    def detect(self, market):

        trend = market.get(
            "trend",
            0
        )

        volatility = market.get(
            "volatility",
            0
        )


        if isinstance(trend,str):

            mapping={
                "UP":1,
                "DOWN":-1,
                "SIDEWAY":0
            }

            trend=mapping.get(
                trend.upper(),
                0
            )


        trend=float(trend)


        if trend >= 0.6 and volatility < 0.4:
            return "BULL"


        if trend <= -0.3:
            return "BEAR"


        return "SIDEWAY"