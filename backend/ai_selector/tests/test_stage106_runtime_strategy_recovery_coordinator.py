from core.runtime_strategy_recovery_coordinator import (
    RuntimeStrategyRecoveryCoordinator
)



def test_runtime_strategy_fallback_recovery():

    coordinator = RuntimeStrategyRecoveryCoordinator()


    result = coordinator.recover(
        {
            "action":
            "fallback_strategy"
        }
    )


    assert (
        result["result"]
        ==
        "strategy_fallback"
    )



def test_runtime_strategy_parameter_recovery():

    coordinator = RuntimeStrategyRecoveryCoordinator()


    result = coordinator.recover(
        {
            "action":
            "adjust_parameters"
        }
    )


    assert (
        result["result"]
        ==
        "parameter_adjustment"
    )



def test_runtime_strategy_recovery_history():

    coordinator = RuntimeStrategyRecoveryCoordinator()


    coordinator.recover(
        {
            "action":
            "fallback_strategy"
        }
    )


    assert len(
        coordinator.recovery_history()
    ) == 1