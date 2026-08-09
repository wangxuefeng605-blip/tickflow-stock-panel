from core.runtime.session_manager import (
    MarketSessionManager
)

from core.runtime.market_scheduler import (
    MarketScheduler
)

from core.market.realtime_provider import (
    RealtimeDataProvider
)


class IntradayScanner:

    def __init__(self):

        self.session = MarketSessionManager()

        self.scheduler = MarketScheduler()

        self.market = RealtimeDataProvider()


    def scan(self):

        print(
            "Realtime market scanning..."
        )

        return [
            {
                "code":"000001",
                "score":1.0
            }
        ]


    def run_once(self):

        print(
            "Running intraday scan..."
        )

        return True


    def run(self):

        while self.session.is_market_open():

            self.run_once()

            self.scheduler.wait()