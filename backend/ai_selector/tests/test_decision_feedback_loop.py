from core.decision.decision_feedback_loop import (
    DecisionFeedbackLoop
)


def test_decision_feedback_loop():

    loop = DecisionFeedbackLoop()


    result = loop.record(
        {
            "action":"SELECT",
            "reward":1
        }
    )


    assert result["stored"] is True

    assert result["reward"] == 1