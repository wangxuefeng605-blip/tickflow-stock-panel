from core.feedback import (
    FeedbackStorage,
    FeedbackEvaluator,
)
from core.feedback.learner import FeedbackLearner


def test_feedback_learner():

    storage = FeedbackStorage()

    storage.save(
        {
            "code": "000001",
            "result": True,
        }
    )

    learner = FeedbackLearner(
        storage,
        FeedbackEvaluator(),
    )

    result = learner.learn()

    assert result["samples"] >= 1
    assert 0 <= result["score"] <= 1
    assert result["status"] == "READY"