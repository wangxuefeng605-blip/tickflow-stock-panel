from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_exploration_controller import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveExplorationController
)



def test_high_fitness_exploit():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveExplorationController()
    )


    result = controller.adjust(
        0.9
    )


    assert result["mode"] == "exploit"
    assert result["exploration_rate"] == 0.2



def test_low_fitness_explore():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveExplorationController()
    )


    result = controller.adjust(
        0.2
    )


    assert result["mode"] == "explore"
    assert result["exploration_rate"] == 0.8



def test_middle_balance():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveExplorationController()
    )


    result = controller.adjust(
        0.5
    )


    assert result["mode"] == "balanced"



def test_exploration_history():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveExplorationController()
    )


    controller.adjust(
        0.7
    )


    assert len(
        controller.get_history()
    ) == 1