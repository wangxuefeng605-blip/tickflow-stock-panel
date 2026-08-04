from core.runtime_strategy_recovery_autonomous_decision_engine import (
    RuntimeStrategyRecoveryAutonomousDecisionEngine
)


def test_runtime_strategy_high_confidence():

    engine = (
        RuntimeStrategyRecoveryAutonomousDecisionEngine()
    )


    result = engine.decide(
        {
            "confidence": 0.8
        }
    )


    assert result["policy"] == "restore"
    assert result["approved"] is True



def test_runtime_strategy_low_confidence():

    engine = (
        RuntimeStrategyRecoveryAutonomousDecisionEngine()
    )


    result = engine.decide(
        {
            "confidence": 0.2
        }
    )


    assert result["policy"] == "rollback"



def test_runtime_strategy_decision_history():

    engine = (
        RuntimeStrategyRecoveryAutonomousDecisionEngine()
    )


    engine.decide(
        {
            "confidence": 0.6
        }
    )


    assert len(
        engine.get_history()
    ) == 1