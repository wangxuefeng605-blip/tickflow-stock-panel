from core.learning.daily_feedback_runner import (
    DailyFeedbackRunner
)


def test_learning_loop():

    weights = {
        "momentum":0.35,
        "trend":0.30,
        "quality":0.15,
        "liquidity":0.10,
        "risk":0.10
    }


    runner = DailyFeedbackRunner()

    result = runner.update(
        weights,
        []
    )


    assert result is not None

    assert abs(
        sum(result.values()) - 1
    ) < 0.000001