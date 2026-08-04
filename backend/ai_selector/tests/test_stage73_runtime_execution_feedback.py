from core.runtime_execution_feedback import RuntimeExecutionFeedback


def test_runtime_execution_feedback():

    feedback = RuntimeExecutionFeedback()


    result = feedback.record(
        {
            "execution_completed":True,
            "plan":{
                "tasks":[
                    "scan_pool"
                ]
            }
        }
    )


    assert result["execution_success"] is True

    assert result["feedback_ready"] is True