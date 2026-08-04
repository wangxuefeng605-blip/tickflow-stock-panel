from core.runtime_strategy_recovery_intelligence_orchestrator import (
    RuntimeStrategyRecoveryIntelligenceOrchestrator
)



def test_runtime_strategy_orchestrator_execute():

    engine = (
        RuntimeStrategyRecoveryIntelligenceOrchestrator()
    )


    result = engine.execute(
        {
            "policy": "restore",
            "confidence": 0.8
        }
    )


    assert result["policy"] == "restore"
    assert result["decision"] == "execute"



def test_runtime_strategy_orchestrator_low_confidence():

    engine = (
        RuntimeStrategyRecoveryIntelligenceOrchestrator()
    )


    result = engine.execute(
        {
            "policy": "fallback",
            "confidence": 0.2
        }
    )


    assert result["decision"] == "reject"



def test_runtime_strategy_orchestrator_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceOrchestrator()
    )


    engine.execute(
        {
            "policy": "restore",
            "confidence": 0.9
        }
    )


    assert len(
        engine.get_history()
    ) == 1