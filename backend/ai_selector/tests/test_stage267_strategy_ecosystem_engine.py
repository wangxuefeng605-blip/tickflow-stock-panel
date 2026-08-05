from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_evolution_ecosystem_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionEcosystemEngine
)


def test_register():

    engine = RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionEcosystemEngine()

    result = engine.register_strategy(
        "alpha",
        0.8
    )

    assert result["registered"] is True



def test_compete():

    engine = RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionEcosystemEngine()

    engine.register_strategy(
        "A",
        0.5
    )

    engine.register_strategy(
        "B",
        0.9
    )

    result = engine.compete(
        "A",
        "B"
    )

    assert result["winner"] == "B"

def test_population():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionEcosystemEngine()
    )


    engine.register_strategy(
        "alpha",
        0.8
    )


    result = engine.get_population()


    assert "alpha" in result