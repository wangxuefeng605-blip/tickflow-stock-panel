def test_selector():

    selector=StrategySelector()


    strategy=selector.select(
        Context(
            state="BULL"
        )
    )


    assert strategy=="momentum"