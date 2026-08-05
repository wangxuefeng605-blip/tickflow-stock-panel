from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_evolution_selection_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelectionEngine
)


def test_add_strategy():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelectionEngine()
    )

    result = engine.add_strategy(
        "alpha",
        0.8
    )

    assert result["added"] is True



def test_evaluate():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelectionEngine()
    )

    engine.add_strategy(
        "alpha",
        0.8
    )

    result = engine.evaluate(
        "alpha"
    )

    assert result["fitness"] == 0.8



def test_select():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelectionEngine()
    )

    engine.add_strategy(
        "weak",
        0.3
    )

    engine.add_strategy(
        "strong",
        0.9
    )


    result = engine.select(
        0.5
    )

    assert "strong" in result["survivors"]

    assert "weak" not in result["survivors"]



def test_evolve_generation():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSelectionEngine()
    )

    engine.add_strategy(
        "alpha",
        0.8
    )

    engine.select(
        0.5
    )

    result = engine.evolve_generation()


    assert "alpha" in result["generation_updated"]