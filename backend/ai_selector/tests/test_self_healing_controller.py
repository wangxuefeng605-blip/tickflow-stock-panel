from core.healing.self_healing_controller import (
    SelfHealingController
)



def test_self_healing_success():


    controller = (
        SelfHealingController()
    )


    result = controller.heal(
        [
            {
                "component":"scanner",
                "error":
                    "connection timeout"
            }
        ],
        executor=lambda x: True
    )


    assert (
        result[0]["success"]
        is True
    )


    assert (
        result[0]["decision"]["action"]
        ==
        "RETRY"
    )