from core.runtime_strategy_autonomous_recovery_executor import (
    RuntimeStrategyAutonomousRecoveryExecutor
)



def test_runtime_strategy_recovery_execute_fallback():

    executor = RuntimeStrategyAutonomousRecoveryExecutor()


    result = executor.execute(
        {
            "selected_action": "fallback"
        }
    )


    assert result["executed"] is True
    assert result["status"] == "success"



def test_runtime_strategy_recovery_execute_rollback():

    executor = RuntimeStrategyAutonomousRecoveryExecutor()


    result = executor.execute(
        {
            "selected_action": "rollback"
        }
    )


    assert result["action"] == "rollback"



def test_runtime_strategy_recovery_execution_history():

    executor = RuntimeStrategyAutonomousRecoveryExecutor()


    executor.execute(
        {
            "selected_action": "fallback"
        }
    )


    assert len(
        executor.execution_history()
    ) == 1