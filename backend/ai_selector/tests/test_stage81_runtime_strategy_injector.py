from core.runtime_strategy_injector import RuntimeStrategyInjector


def test_runtime_strategy_injector():

    injector = RuntimeStrategyInjector()


    result = injector.inject(
        {
            "name":"momentum_v2",
            "weight":0.8
        }
    )


    assert result["strategy"] == "momentum_v2"

    assert injector.current()["weight"] == 0.8