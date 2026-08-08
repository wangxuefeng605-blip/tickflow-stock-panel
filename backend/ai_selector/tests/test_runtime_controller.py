from core.runtime.runtime_controller import RuntimeController


def test_runtime_controller():

    controller = RuntimeController()


    result = controller.execute(
        {
            "decision":
            {
                "action":"BUY"
            }
        }
    )


    assert result["decision"]["action"] == "BUY"