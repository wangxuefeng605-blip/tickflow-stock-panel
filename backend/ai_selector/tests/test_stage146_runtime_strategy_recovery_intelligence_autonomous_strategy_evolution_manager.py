from core.runtime_strategy_recovery_intelligence_autonomous_strategy_evolution_manager import (
    RuntimeStrategyRecoveryIntelligenceAutonomousStrategyEvolutionManager
)



def test_strategy_evolution_active():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyEvolutionManager()
    )


    result = manager.evolve(
        {
            "strategy_score": 0.8
        }
    )


    assert result["version"] == 2
    assert result["fitness"] == 0.8
    assert result["status"] == "active"



def test_strategy_evolution_deprecated():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyEvolutionManager()
    )


    result = manager.evolve(
        {
            "strategy_score": 0.2
        }
    )


    assert result["status"] == "deprecated"



def test_strategy_active_selection():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyEvolutionManager()
    )


    manager.evolve(
        {
            "strategy_score": 0.4
        }
    )


    manager.evolve(
        {
            "strategy_score": 0.9
        }
    )


    result = manager.get_active_strategy()


    assert result["fitness"] == 0.9



def test_strategy_history():

    manager = (
        RuntimeStrategyRecoveryIntelligenceAutonomousStrategyEvolutionManager()
    )


    manager.evolve(
        {
            "strategy_score": 0.7
        }
    )


    assert len(
        manager.get_history()
    ) == 1