from core.runtime_strategy_recovery_intelligence_autonomous_decision_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousDecisionEngine
)



def test_autonomous_decision_execute():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousDecisionEngine()
    )


    result = engine.decide(
        {
            "policy": "restore",
            "confidence": 0.8
        }
    )


    assert result["action"] == "execute"
    assert result["policy"] == "restore"
    assert result["risk"] == 0.2
    assert result["allowed"] is True



def test_autonomous_decision_reject():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousDecisionEngine()
    )


    result = engine.decide(
        {
            "policy": "fallback",
            "confidence": 0.2
        }
    )


    assert result["action"] == "reject"
    assert result["allowed"] is False



def test_autonomous_decision_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousDecisionEngine()
    )


    engine.decide(
        {
            "policy": "restore",
            "confidence": 0.9
        }
    )


    assert len(
        engine.get_history()
    ) == 1