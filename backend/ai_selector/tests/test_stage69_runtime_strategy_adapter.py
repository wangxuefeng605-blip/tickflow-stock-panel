from core.runtime_strategy_adapter import RuntimeStrategyAdapter


def test_runtime_strategy_adapter():

    adapter = RuntimeStrategyAdapter()


    result = adapter.adapt(
        {
            "preferred_mode":"AGGRESSIVE",
            "confidence":0.8
        }
    )


    assert result["workers"] == 8

    assert result["retry_enabled"] is True