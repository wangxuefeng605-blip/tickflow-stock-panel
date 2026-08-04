from core.retry_feedback import RetryFeedback


def test_retry_feedback():

    feedback = RetryFeedback()


    result = feedback.process(
        {
            "retry_completed": True,
            "retry_count": 1
        }
    )


    assert result["feedback_received"] is True

    assert result["retry_completed"] is True

    assert result["retry_count"] == 1