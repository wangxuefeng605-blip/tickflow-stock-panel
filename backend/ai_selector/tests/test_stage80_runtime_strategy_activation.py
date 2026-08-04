from core.runtime_strategy_activation import RuntimeStrategyActivation


def test_runtime_strategy_activation():

    runtime = RuntimeStrategyActivation()


    result = runtime.activate(
        {
            "name":"momentum_v2",
            "weight":0.8
        }
    )


    assert result["activated"] is True

    assert runtime.current()["name"] == "momentum_v2"