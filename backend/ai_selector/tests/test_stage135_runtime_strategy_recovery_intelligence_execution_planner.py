from core.runtime_strategy_recovery_intelligence_execution_planner import (
    RuntimeStrategyRecoveryIntelligenceExecutionPlanner
)



def test_execution_plan_generate():

    planner = (
        RuntimeStrategyRecoveryIntelligenceExecutionPlanner()
    )


    result = planner.plan(
        {
            "decision": "accept",
            "policy": "restore",
            "execution_ready": True
        }
    )


    assert result["plan"] == "execute_recovery"
    assert result["validation"] is True



def test_execution_plan_reject():

    planner = (
        RuntimeStrategyRecoveryIntelligenceExecutionPlanner()
    )


    result = planner.plan(
        {
            "decision": "reject",
            "execution_ready": False
        }
    )


    assert result["plan"] is None
    assert result["validation"] is False



def test_execution_history():

    planner = (
        RuntimeStrategyRecoveryIntelligenceExecutionPlanner()
    )


    planner.plan(
        {
            "execution_ready": True,
            "policy": "fallback"
        }
    )


    assert len(
        planner.get_history()
    ) == 1