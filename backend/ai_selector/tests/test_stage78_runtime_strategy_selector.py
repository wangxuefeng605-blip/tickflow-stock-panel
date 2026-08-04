from core.runtime_strategy_selector import RuntimeStrategySelector


def test_runtime_strategy_selector():

    selector = RuntimeStrategySelector()


    result = selector.select(
        [
            {
                "version":1,
                "score":0.5
            },
            {
                "version":2,
                "score":0.9
            }
        ]
    )


    assert result["version"] == 2