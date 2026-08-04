from core.runtime_strategy_recovery_autonomous_execution_controller import (
    RuntimeStrategyRecoveryAutonomousExecutionController
)


def test_runtime_strategy_restore_execution():

    controller = (
        RuntimeStrategyRecoveryAutonomousExecutionController()
    )


    result = controller.execute(
        {
            "policy": "restore",
            "approved": True
        }
    )


    assert result["action"] == "restore"
    assert result["status"] == "executed"



def test_runtime_strategy_block_execution():

    controller = (
        RuntimeStrategyRecoveryAutonomousExecutionController()
    )


    result = controller.execute(
        {
            "policy": "rollback",
            "approved": False
        }
    )


    assert result["status"] == "blocked"



def test_runtime_strategy_execution_history():

    controller = (
        RuntimeStrategyRecoveryAutonomousExecutionController()
    )


    controller.execute(
        {
            "policy": "fallback",
            "approved": True
        }
    )


    assert len(
        controller.get_history()
    ) == 1