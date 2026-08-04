from core.runtime_decision_feedback import RuntimeDecisionFeedback



def test_runtime_decision_feedback():

    feedback = RuntimeDecisionFeedback()


    result = feedback.record(
        {
            "decision":"AGGRESSIVE",
            "workers":8,
            "success":True
        }
    )


    assert result["success"] is True


    latest = feedback.latest()


    assert latest["decision"] == "AGGRESSIVE"