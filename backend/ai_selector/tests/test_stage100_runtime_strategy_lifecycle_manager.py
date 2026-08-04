from core.runtime_strategy_lifecycle_manager import (
    RuntimeStrategyLifecycleManager
)


def test_runtime_strategy_lifecycle_manager(tmp_path):

    manager = RuntimeStrategyLifecycleManager()

    state = manager.initialize()

    assert state is not None


    result = manager.activate()

    assert result["activated"] is True


    updated = manager.update(
        {
            "momentum_weight": 0.4
        }
    )


    assert (
        updated["momentum_weight"]
        ==
        0.4
    )


    saved = manager.persist()

    assert saved["saved"] is True



def test_runtime_strategy_lifecycle_execute():

    manager = RuntimeStrategyLifecycleManager()

    result = manager.lifecycle()

    assert result["success"] is True