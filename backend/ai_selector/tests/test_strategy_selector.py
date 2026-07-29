from core.strategy.selector import StrategySelector


def test_selector():

    selector = StrategySelector()


    strategy = selector.select(
        "BULL"
    )


    assert strategy == "momentum"