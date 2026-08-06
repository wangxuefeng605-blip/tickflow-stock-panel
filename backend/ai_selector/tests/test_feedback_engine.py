from core.learning.feedback_engine import (
    FeedbackLearningEngine
)


def test_feedback_engine():

    engine = FeedbackLearningEngine()


    weights = {
        "momentum":0.35,
        "trend":0.30,
        "quality":0.15,
        "liquidity":0.10,
        "risk":0.10
    }


    feedback = [
        {
            "code":"000001",
            "score":90,
            "return":0.1
        },
        {
            "code":"000002",
            "score":80,
            "return":0.05
        }
    ]


    result = engine.update_weights(
        weights,
        feedback
    )


    assert "weights" in result
    assert "performance" in result
    assert "learning" in result

    assert abs(
        sum(result["weights"].values()) - 1
    ) < 0.000001