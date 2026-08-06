from core.learning.daily_feedback_runner import (
    DailyFeedbackRunner
)


def test_daily_feedback_update():

    runner = DailyFeedbackRunner()


    weights = {
        "momentum":0.35,
        "trend":0.30,
        "quality":0.15,
        "liquidity":0.10,
        "risk":0.10
    }


    feedbacks = [
        {
            "code":"000001",
            "score":90,
            "return":0.1
        }
    ]


    result = runner.update(
        weights,
        feedbacks
    )


    assert abs(
        sum(result.values()) - 1
    ) < 0.000001