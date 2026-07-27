class WeightEngine:


    DEFAULT = {

        "momentum": 0.25,

        "trend": 0.25,

        "quality": 0.20,

        "liquidity": 0.15,

        "risk": 0.15
    }



    def get_weights(
        self,
        market_state
    ):


        if market_state == "BULL":

            return {

                "momentum":0.35,

                "trend":0.30,

                "quality":0.15,

                "liquidity":0.10,

                "risk":0.10
            }


        if market_state == "BEAR":

            return {

                "momentum":0.10,

                "trend":0.15,

                "quality":0.30,

                "liquidity":0.20,

                "risk":0.25
            }


        return self.DEFAULT.copy()