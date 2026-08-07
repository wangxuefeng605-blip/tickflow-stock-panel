from core.healing.healing_feedback import (
    HealingFeedback
)



def test_feedback_learning():


    feedback = HealingFeedback()


    feedback.record(
        "TIMEOUT",
        {
            "retry":3
        },
        True
    )


    feedback.record(
        "TIMEOUT",
        {
            "retry":3
        },
        True
    )


    assert (
        feedback.success_rate()
        ==
        1
    )


    assert (
        feedback.recommend()["mode"]
        ==
        "KEEP"
    )