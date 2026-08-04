from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_knowledge_reasoning_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryKnowledgeReasoningEngine
)



def test_learn_pattern():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryKnowledgeReasoningEngine()
    )


    result = engine.learn_pattern(
        {
            "strategy": "trend",
            "fitness": 0.9
        }
    )


    assert result["strategy"] == "trend"



def test_reason_best_pattern():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryKnowledgeReasoningEngine()
    )


    engine.learn_pattern(
        {
            "strategy": "a",
            "fitness": 0.5
        }
    )


    engine.learn_pattern(
        {
            "strategy": "b",
            "fitness": 0.95
        }
    )


    result = engine.reason()


    assert result["recommended_strategy"]["strategy"] == "b"



def test_empty_reason():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryKnowledgeReasoningEngine()
    )


    assert engine.reason() is None



def test_reason_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryKnowledgeReasoningEngine()
    )


    engine.learn_pattern(
        {
            "fitness": 1
        }
    )


    engine.reason()


    assert len(
        engine.get_history()
    ) == 2