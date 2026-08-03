from core.decision import DecisionFeedback


def test_decision_feedback():


    feedback = DecisionFeedback()


    result = feedback.evaluate(
        "000001",
        {
            "return":0.05
        }
    )


    assert result is None or isinstance(
        result,
        dict
    )