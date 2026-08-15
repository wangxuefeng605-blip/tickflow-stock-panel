class MarketSnapshot:


    def __init__(self, provider):

        self.provider = provider

        self._data = []


    def refresh(self):

        self._data = (
            self.provider
            .get_market_data()
        )

        return self._data


    def get_all(self):

        return self._data


    def count(self):

        return len(
            self._data
        )