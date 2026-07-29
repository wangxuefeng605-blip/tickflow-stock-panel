class MarketDataProvider:


    def get_market_data(self):

        return {

            "index_change": 0.5,

            "volume_ratio": 1.2,

            "volatility": 0.18,

            "trend": "UP",

            "breadth": 0.6

        }



def get_market_data():

    return MarketDataProvider().get_market_data()