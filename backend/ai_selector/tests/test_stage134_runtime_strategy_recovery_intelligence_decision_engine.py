from core.runtime_strategy_recovery_intelligence_decision_engine import (
    RuntimeStrategyRecoveryIntelligenceDecisionEngine
)



def test_decision_accept():

    engine = (
        RuntimeStrategyRecoveryIntelligenceDecisionEngine()
    )


    result = engine.decide(
        {
            "policy": "restore",
            "confidence": 0.9
        }
    )


    assert result["decision"] == "accept"
    assert result["policy"] == "restore"
    assert result["execution_ready"] is True



def test_decision_reject():

    engine = (
        RuntimeStrategyRecoveryIntelligenceDecisionEngine()
    )


    result = engine.decide(
        {
            "policy": None,
            "confidence": 0
        }
    )


    assert result["decision"] == "reject"
    assert result["execution_ready"] is False



def test_decision_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceDecisionEngine()
    )


    engine.decide(
        {
            "policy": "fallback",
            "confidence": 0.8
        }
    )


    assert len(
        engine.get_history()
    ) == 1