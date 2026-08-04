from core.runtime_strategy_recovery_intelligence_autonomous_evolution_population_manager import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPopulationManager
)



def test_add_strategy():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPopulationManager()
    )


    manager.add_strategy(
        {
            "strategy": "restore",
            "fitness": 0.8
        }
    )


    assert len(
        manager.get_population()
    ) == 1



def test_population_evolution():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPopulationManager(
            max_size=2
        )
    )


    manager.add_strategy(
        {
            "strategy": "a",
            "fitness": 0.5
        }
    )

    manager.add_strategy(
        {
            "strategy": "b",
            "fitness": 0.9
        }
    )

    manager.add_strategy(
        {
            "strategy": "c",
            "fitness": 0.1
        }
    )


    result = manager.evolve()


    assert len(
        result["population"]
    ) == 2

    assert result["population"][0]["strategy"] == "b"



def test_elite_strategy():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPopulationManager()
    )


    manager.add_strategy(
        {
            "strategy": "best",
            "fitness": 1
        }
    )


    elite = manager.get_elite()


    assert elite["strategy"] == "best"



def test_population_history():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionPopulationManager()
    )


    manager.add_strategy(
        {
            "strategy": "test",
            "fitness": 0.5
        }
    )


    assert len(
        manager.get_history()
    ) == 1