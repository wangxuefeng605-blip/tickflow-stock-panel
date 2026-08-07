from core.runtime.recovery_controller import (
    AutonomousRecoveryController
)


def test_recovery_controller_success():

    controller = (
        AutonomousRecoveryController()
    )


    result = controller.execute(
        {
            "mode": "RECOVERY"
        },
        lambda: "OK"
    )


    assert result["status"] == "RECOVERED"
    assert result["result"] == "OK"



def test_recovery_controller_skip():

    controller = (
        AutonomousRecoveryController()
    )


    result = controller.execute(
        {
            "mode": "NORMAL"
        },
        lambda: "OK"
    )


    assert result["status"] == "SKIPPED"