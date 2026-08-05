from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_genetic_recombination_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyGeneticRecombinationEngine
)



def test_add_genome():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyGeneticRecombinationEngine()
    )


    result = engine.add_genome(
        "A",
        {
            "momentum":0.5
        },
        0.8
    )


    assert result["stored"] is True



def test_recombine():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyGeneticRecombinationEngine()
    )


    engine.add_genome(
        "A",
        {
            "momentum":0.5
        },
        0.8
    )


    engine.add_genome(
        "B",
        {
            "trend":0.6
        },
        0.6
    )


    result = engine.recombine(
        "A",
        "B"
    )


    assert result["child"]["fitness"] == 0.7



def test_best_child():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyGeneticRecombinationEngine()
    )


    engine.add_genome(
        "A",
        {},
        1
    )


    engine.add_genome(
        "B",
        {},
        0.5
    )


    engine.recombine(
        "A",
        "B"
    )


    result = engine.best_child()


    assert result["fitness"] == 0.75



def test_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyGeneticRecombinationEngine()
    )


    engine.add_genome(
        "test",
        {},
        0.5
    )


    assert len(
        engine.get_history()
    ) == 1