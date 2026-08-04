from core.runtime_strategy_recovery_intelligence_memory_engine import (
    RuntimeStrategyRecoveryIntelligenceMemoryEngine
)



def test_memory_store():

    engine = (
        RuntimeStrategyRecoveryIntelligenceMemoryEngine()
    )


    result = engine.remember(
        {
            "policy": "restore",
            "success": True
        }
    )


    assert result["stored"] is True



def test_memory_recall():

    engine = (
        RuntimeStrategyRecoveryIntelligenceMemoryEngine()
    )


    engine.remember(
        {
            "policy": "restore",
            "success": True
        }
    )

    engine.remember(
        {
            "policy": "fallback",
            "success": False
        }
    )


    result = engine.recall(
        "restore"
    )


    assert len(result) == 1
    assert result[0]["policy"] == "restore"



def test_memory_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceMemoryEngine()
    )


    engine.remember(
        {
            "policy": "restore"
        }
    )


    assert len(
        engine.history()
    ) == 1