from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_mutation_generation_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyMutationGenerationEngine
)



def test_mutation_create():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyMutationGenerationEngine()
    )


    engine.add_strategy(
        "trend",
        {
            "risk":0.5
        }
    )


    result = engine.mutate(
        "trend"
    )


    assert (
        result["child"]
        ==
        "trend_mutation"
    )



def test_generated_list():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyMutationGenerationEngine()
    )


    engine.add_strategy(
        "A",
        {
            "x":0.4
        }
    )


    engine.mutate(
        "A"
    )


    assert len(
        engine.get_generated()
    ) == 1



def test_population_generation():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyMutationGenerationEngine()
    )


    engine.add_strategy(
        "A",
        {
            "x":0.4
        }
    )


    result = engine.generate_population(
        1
    )


    assert len(result) == 1