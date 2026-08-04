from core.runtime_strategy_recovery_intelligence_autonomous_evolution_predictive_strategy_generator import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPredictiveStrategyGenerator
)



def test_strategy_generation():

    generator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPredictiveStrategyGenerator()
    )


    result = generator.generate(
        {
            "source_strategy": "restore",
            "recommended_strategy": "adaptive_restore"
        }
    )


    assert "adaptive_restore" in result["candidates"]



def test_strategy_generation_without_recommendation():

    generator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPredictiveStrategyGenerator()
    )


    result = generator.generate(
        {
            "source_strategy": "restore",
            "recommended_strategy": None
        }
    )


    assert result["candidates"] == [
        "adaptive_restore"
    ]



def test_strategy_mutation():

    generator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPredictiveStrategyGenerator()
    )


    result = generator.mutate(
        "restore"
    )


    assert result == "adaptive_restore"



def test_generation_history():

    generator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPredictiveStrategyGenerator()
    )


    generator.generate(
        {
            "source_strategy": "test"
        }
    )


    assert len(
        generator.get_history()
    ) == 1