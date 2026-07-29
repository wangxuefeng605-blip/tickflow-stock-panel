from core.strategy.engine import StrategyEngine


def test_strategy():

    engine=StrategyEngine()


    result=engine.evaluate(
        {
            "momentum":0.1,
            "trend":1
        }
    )


    assert result["action"]=="BUY"