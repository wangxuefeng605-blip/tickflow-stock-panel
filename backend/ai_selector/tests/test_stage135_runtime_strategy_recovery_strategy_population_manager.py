from core.runtime_strategy_recovery_strategy_population_manager import (
    RuntimeStrategyRecoveryStrategyPopulationManager
)



def test_strategy_population_register():

    manager = (
        RuntimeStrategyRecoveryStrategyPopulationManager()
    )


    manager.register_strategy(
        "restore",
        0.8
    )


    assert (
        "restore"
        in manager.population
    )



def test_strategy_population_select_best():

    manager = (
        RuntimeStrategyRecoveryStrategyPopulationManager()
    )


    manager.register_strategy(
        "restore",
        0.8
    )

    manager.register_strategy(
        "fallback",
        0.5
    )


    best = (
        manager.select_best()
    )


    assert best == "restore"



def test_strategy_population_history():

    manager = (
        RuntimeStrategyRecoveryStrategyPopulationManager()
    )


    manager.register_strategy(
        "restore",
        0.8
    )


    manager.evaluate(
        {
            "restore":0.9
        }
    )


    assert len(
        manager.get_history()
    ) == 1