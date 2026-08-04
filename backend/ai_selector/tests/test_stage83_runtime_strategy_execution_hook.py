from core.runtime_strategy_execution_hook import RuntimeStrategyExecutionHook


def test_runtime_strategy_execution_hook():

    hook = RuntimeStrategyExecutionHook()


    result = hook.prepare(
        {
            "strategy":"momentum_v2",
            "weight":0.8
        }
    )


    assert result["active"] is True

    assert hook.current()["strategy"] == "momentum_v2"