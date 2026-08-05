from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_evolution_mutation_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionMutationEngine
)



def test_register():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionMutationEngine()
    )


    result = engine.register_strategy(
        "momentum",
        {
            "weight":0.5
        }
    )


    assert result["registered"] is True



def test_mutation():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionMutationEngine()
    )


    engine.register_strategy(
        "trend",
        {
            "weight":0.5
        }
    )


    result = engine.mutate_parameter(
        "trend",
        "weight",
        0.1
    )


    assert result["new"] == 0.6



def test_variant():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionMutationEngine()
    )


    engine.register_strategy(
        "alpha",
        {
            "risk":0.3
        }
    )


    result = engine.create_variant(
        "alpha",
        "alpha_v2"
    )


    assert result["created"] is True



def test_compare():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionMutationEngine()
    )


    engine.register_strategy(
        "A",
        {
            "x":1
        }
    )


    engine.create_variant(
        "A",
        "B"
    )


    result = engine.compare(
        "A",
        "B"
    )


    assert result["first"]["x"] == 1