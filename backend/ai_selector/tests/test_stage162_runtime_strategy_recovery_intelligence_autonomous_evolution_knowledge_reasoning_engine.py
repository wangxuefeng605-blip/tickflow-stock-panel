from core.runtime_strategy_recovery_intelligence_autonomous_evolution_knowledge_reasoning_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeReasoningEngine
)



def test_reason_strategy():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeReasoningEngine()
    )


    result = engine.reason(
        {
            "nodes": [],
            "edges": [
                {
                    "source": "restore",
                    "target": "adaptive_restore",
                    "relation": "evolved_from"
                }
            ]
        },
        "restore"
    )


    assert result["recommended_strategy"] == "adaptive_restore"
    assert result["confidence"] == 0.8



def test_reason_unknown():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeReasoningEngine()
    )


    result = engine.reason(
        {
            "nodes": [],
            "edges": []
        },
        "unknown"
    )


    assert result["recommended_strategy"] is None



def test_strategy_compare():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeReasoningEngine()
    )


    result = engine.compare(
        [
            {
                "strategy": "a",
                "fitness": 0.5
            },
            {
                "strategy": "b",
                "fitness": 0.9
            }
        ]
    )


    assert result["strategy"] == "b"



def test_reason_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionKnowledgeReasoningEngine()
    )


    engine.reason(
        {
            "edges": []
        },
        "test"
    )


    assert len(
        engine.get_history()
    ) == 1