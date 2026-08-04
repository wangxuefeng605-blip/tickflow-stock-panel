from core.runtime_strategy_auto_recovery_manager import (
    RuntimeStrategyAutoRecoveryManager
)


def test_runtime_strategy_recovery():

    manager = RuntimeStrategyAutoRecoveryManager()


    state = {
        "strategy": "momentum",
        "version": 1
    }


    result = manager.save_checkpoint(
        state
    )

    assert result["saved"] is True


    manager.update_state(
        {
            "broken": True
        }
    )


    rollback = (
        manager.rollback_if_invalid()
    )


    assert rollback["rollback"] is True



def test_runtime_strategy_fallback():

    manager = RuntimeStrategyAutoRecoveryManager()


    result = (
        manager.fallback_strategy()
    )


    assert result["fallback"] is True

    assert (
        result["state"]["strategy"]
        ==
        "default"
    )