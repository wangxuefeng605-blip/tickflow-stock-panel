from core.intelligence.state_engine import MarketStateEngine



def test_bull():

    engine = MarketStateEngine()


    assert engine.detect(
        {
            "trend":0.8,
            "volatility":0.2
        }
    )=="BULL"



def test_bear():

    engine = MarketStateEngine()


    assert engine.detect(
        {
            "trend":0.1,
            "volatility":0.5
        }
    )=="BEAR"



def test_sideway():

    engine = MarketStateEngine()


    assert engine.detect(
        {
            "trend":0.45,
            "volatility":0.3
        }
    )=="SIDEWAY"