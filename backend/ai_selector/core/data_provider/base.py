from abc import ABC, abstractmethod


class MarketDataProvider(ABC):

    """
    Market Data Provider Interface
    """

    @abstractmethod
    def get_market_data(self):

        """
        Return normalized market data

        Example:

        [
            {
                "code": "000001",
                "price": 10.5,
                "volume": 1000000
            }
        ]

        """

        pass