from datetime import datetime, time


class MarketSessionManager:


    def is_market_open(self):

        now = datetime.now().time()

        morning = (
            time(9, 30)
            <= now
            <= time(11, 30)
        )

        afternoon = (
            time(13, 0)
            <= now
            <= time(15, 0)
        )

        return (
            morning
            or afternoon
        )