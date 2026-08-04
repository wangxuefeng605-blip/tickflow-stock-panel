from core.runtime_strategy_execution_manager import RuntimeStrategyExecutionManager


def test_runtime_strategy_execution_manager():

    manager = RuntimeStrategyExecutionManager()


    result = manager.execute(
        {
            "name":"momentum"
        }
    )


    assert result["executed"] is True
    assert result["strategy"]["name"] == "momentum"