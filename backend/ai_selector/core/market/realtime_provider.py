from datetime import datetime

from core.market.market_snapshot import (
    MarketSnapshot
)


class RealtimeDataProvider:


    def get_quote(
        self,
        code
    ):

        return MarketSnapshot(
            code=code,
            price=0,
            change_pct=0,
            volume=0,
            timestamp=datetime.now()
        )