from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_strategy_evolution_simulation_universe_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSimulationUniverseEngine
)



def test_create_environment():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSimulationUniverseEngine()
    )


    result = engine.create_environment(
        "bull_market",
        "BULL"
    )


    assert result["created"] is True



def test_add_strategy():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSimulationUniverseEngine()
    )


    engine.create_environment(
        "test",
        "SIDEWAY"
    )


    result = engine.add_strategy(
        "test",
        "momentum"
    )


    assert result["added"] is True



def test_simulation():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSimulationUniverseEngine()
    )


    engine.create_environment(
        "market",
        "BEAR"
    )


    engine.add_strategy(
        "market",
        "value"
    )


    result = engine.simulate(
        "market",
        10
    )


    assert result["rounds"] == 10



def test_best_strategy():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionStrategyEvolutionSimulationUniverseEngine()
    )


    simulation = {

        "results":[
            {
                "strategy":"A",
                "score":0.5
            },
            {
                "strategy":"B",
                "score":0.8
            }
        ]

    }


    result = engine.best_strategy(
        simulation
    )


    assert result["strategy"] == "B"