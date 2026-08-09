from core.factor.realtime_factor import (
    RealtimeFactorEngine
)

from core.market.market_snapshot import (
    MarketSnapshot
)

from datetime import datetime



def test_realtime_factor():


    engine = (
        RealtimeFactorEngine()
    )


    snapshot = MarketSnapshot(

        code="000820",

        price=12.5,

        change_pct=5,

        volume=8000000,

        timestamp=datetime.now()
    )


    result = (
        engine.calculate(
            snapshot
        )
    )


    assert result["momentum"] > 0

    assert result["trend"] > 0

    assert (
        result["volume_strength"]
        > 0
    )