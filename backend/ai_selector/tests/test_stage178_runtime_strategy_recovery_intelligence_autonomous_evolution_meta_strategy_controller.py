from core.runtime_strategy_recovery_intelligence_autonomous_evolution_meta_strategy_controller import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMetaStrategyController
)



def test_register_strategy():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMetaStrategyController()
    )


    result = controller.register_strategy(
        "aggressive",
        {
            "mutation": 0.3
        }
    )


    assert result["mutation"] == 0.3

    assert (
        "aggressive"
        in controller.get_strategies()
    )



def test_select_strategy():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMetaStrategyController()
    )


    controller.register_strategy(
        "stable",
        {
            "mutation": 0.05
        }
    )


    result = controller.select_strategy(
        "stable"
    )


    assert result["selected"] == "stable"

    assert (
        controller.get_active_strategy()
        ==
        "stable"
    )



def test_unknown_strategy():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMetaStrategyController()
    )


    result = controller.select_strategy(
        "unknown"
    )


    assert result is None



def test_strategy_history():

    controller = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionMetaStrategyController()
    )


    controller.register_strategy(
        "test",
        {}
    )


    assert len(
        controller.get_history()
    ) == 1