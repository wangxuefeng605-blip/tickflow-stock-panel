from .base import MarketDataProvider


class MockMarketDataProvider(
    MarketDataProvider
):


    def get_market_data(self):

        return [

            {
                "code": "000001",
                "price": 10,
                "volume": 1000000,

                "factors": {

                    "momentum":0.8,
                    "trend":1

                }
            },


            {
                "code": "000002",
                "price":20,
                "volume":800000,

                "factors":{

                    "momentum":0.5,
                    "trend":0.5

                }
            }

        ]