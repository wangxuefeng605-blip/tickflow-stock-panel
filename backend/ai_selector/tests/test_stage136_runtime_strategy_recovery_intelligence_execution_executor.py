from core.runtime_strategy_recovery_intelligence_execution_executor import (
    RuntimeStrategyRecoveryIntelligenceExecutionExecutor
)



def test_execution_success():

    executor = (
        RuntimeStrategyRecoveryIntelligenceExecutionExecutor()
    )


    result = executor.execute(
        {
            "validation": True,
            "steps": [
                "prepare",
                "apply_policy",
                "verify"
            ]
        }
    )


    assert result["status"] == "completed"
    assert result["success"] is True



def test_execution_failure():

    executor = (
        RuntimeStrategyRecoveryIntelligenceExecutionExecutor()
    )


    result = executor.execute(
        {
            "validation": False
        }
    )


    assert result["success"] is False
    assert result["error"] == "invalid_plan"



def test_execution_history():

    executor = (
        RuntimeStrategyRecoveryIntelligenceExecutionExecutor()
    )


    executor.execute(
        {
            "validation": True,
            "steps": []
        }
    )


    assert len(
        executor.get_history()
    ) == 1