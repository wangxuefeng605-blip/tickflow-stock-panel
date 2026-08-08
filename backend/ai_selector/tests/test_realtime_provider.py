from core.market.realtime_provider import (
    RealtimeDataProvider
)


def test_realtime_provider():

    provider = (
        RealtimeDataProvider()
    )


    result = (
        provider.get_quote(
            "000820"
        )
    )


    assert result.code == "000820"

    assert result.price == 0