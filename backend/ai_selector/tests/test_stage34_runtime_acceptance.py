from core.runtime.runtime_controller import RuntimeController
from core.runtime.runtime_feedback import RuntimeFeedback


def test_stage34_full_runtime_loop():

    controller = RuntimeController()

    runtime_result = controller.execute(
        {
            "decision":
            {
                "action":"BUY"
            },

            "execution":
            {
                "status":"DONE"
            },

            "portfolio":
            {
                "risk":0.2
            },

            "strategy":
            {
                "name":"momentum"
            }
        }
    )


    feedback = RuntimeFeedback()


    result = feedback.collect(
        runtime_result
    )


    assert result["status"] == "COMPLETED"

    assert (
        result["result"]["decision"]["action"]
        ==
        "BUY"
    )