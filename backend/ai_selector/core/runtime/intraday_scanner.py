from core.runtime.session_manager import (
    MarketSessionManager
)

from core.runtime.market_scheduler import (
    MarketScheduler
)


class IntradayScanner:


    def __init__(self):

        self.session = (
            MarketSessionManager()
        )

        self.scheduler = (
            MarketScheduler()
        )



    def run_once(self):

        print(
            "Running intraday scan..."
        )

        return True



    def run(self):

        while (
            self.session.is_market_open()
        ):

            self.run_once()

            self.scheduler.wait()