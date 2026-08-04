from core.runtime_strategy_recovery_decision_guard_engine import (
    RuntimeStrategyRecoveryDecisionGuardEngine
)


def test_runtime_strategy_auto_execute():

    engine = (
        RuntimeStrategyRecoveryDecisionGuardEngine()
    )


    result = engine.guard(
        {
            "policy": "restore",
            "risk": 0.2
        }
    )


    assert result["action"] == "AUTO_EXECUTE"



def test_runtime_strategy_block():

    engine = (
        RuntimeStrategyRecoveryDecisionGuardEngine()
    )


    result = engine.guard(
        {
            "policy": "rollback",
            "risk": 0.9
        }
    )


    assert result["action"] == "BLOCK"



def test_runtime_strategy_guard_history():

    engine = (
        RuntimeStrategyRecoveryDecisionGuardEngine()
    )


    engine.guard(
        {
            "policy": "fallback",
            "risk": 0.5
        }
    )


    assert len(
        engine.get_history()
    ) == 1