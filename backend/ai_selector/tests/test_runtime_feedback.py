from core.runtime.runtime_feedback import RuntimeFeedback



def test_runtime_feedback():


    feedback = RuntimeFeedback()


    result = feedback.collect(
        {
            "decision":
            {
                "action":"BUY"
            }
        }
    )


    assert result["status"] == "COMPLETED"

    assert result["result"]["decision"]["action"] == "BUY"