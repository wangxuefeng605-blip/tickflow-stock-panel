from core.data_provider import (
    MockMarketDataProvider,
    MarketSnapshot
)



def test_market_snapshot():


    provider = (
        MockMarketDataProvider()
    )


    snapshot = MarketSnapshot(
        provider
    )


    data = snapshot.refresh()


    assert len(data)==2


    assert (
        snapshot.count()
        ==2
    )


    stocks = (
        snapshot.get_all()
    )


    assert stocks[0]["code"]=="000001"