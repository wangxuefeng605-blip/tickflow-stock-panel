from core.runtime_strategy_adaptive_recovery_planner import (
    RuntimeStrategyAdaptiveRecoveryPlanner
)



def test_runtime_strategy_adaptive_recovery_plan():

    planner = RuntimeStrategyAdaptiveRecoveryPlanner()


    result = planner.plan(
        {
            "history": [
                {
                    "action": "fallback",
                    "success": True
                },
                {
                    "action": "fallback",
                    "success": True
                },
                {
                    "action": "rollback",
                    "success": False
                }
            ]
        }
    )


    assert result["selected_action"] == "fallback"



def test_runtime_strategy_adaptive_recovery_default():

    planner = RuntimeStrategyAdaptiveRecoveryPlanner()


    result = planner.plan({})


    assert result["selected_action"] == "fallback"



def test_runtime_strategy_adaptive_recovery_history():

    planner = RuntimeStrategyAdaptiveRecoveryPlanner()


    planner.plan({})


    assert len(
        planner.planner_history()
    ) == 1