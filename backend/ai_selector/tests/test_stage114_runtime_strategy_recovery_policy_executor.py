from core.runtime_strategy_recovery_policy_executor import (
    RuntimeStrategyRecoveryPolicyExecutor
)



def test_runtime_strategy_recovery_policy_execute():

    executor = RuntimeStrategyRecoveryPolicyExecutor()


    result = executor.execute(
        {
            "selected_policy": "fallback"
        }
    )


    assert result["policy"] == "fallback"
    assert result["status"] == "executed"



def test_runtime_strategy_recovery_policy_execute_other():

    executor = RuntimeStrategyRecoveryPolicyExecutor()


    result = executor.execute(
        {
            "selected_policy": "rollback"
        }
    )


    assert result["status"] == "executed"



def test_runtime_strategy_recovery_policy_execution_history():

    executor = RuntimeStrategyRecoveryPolicyExecutor()


    executor.execute(
        {
            "selected_policy": "parameter_restore"
        }
    )


    assert len(
        executor.execution_history()
    ) == 1