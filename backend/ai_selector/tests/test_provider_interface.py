from core.data_provider import (
    MockMarketDataProvider
)



def test_provider_interface():

    provider = (
        MockMarketDataProvider()
    )


    data = (
        provider.get_market_data()
    )


    assert isinstance(
        data,
        list
    )


    assert "code" in data[0]