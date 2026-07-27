from core.intelligence.market_provider import get_market_data


def test_market_provider():

    data = get_market_data()


    assert "trend" in data

    assert "volatility" in data

    assert "breadth" in data