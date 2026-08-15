from core.feedback.learning_service import (
    FeedbackLearningService
)


class FakeStorage:

    def load(self):

        return [
            {
                "stock_code": "000001",
                "prediction": "BUY",
                "actual_result": "WIN",
                "score": 1
            },
            {
                "stock_code": "000002",
                "prediction": "BUY",
                "actual_result": "LOSS",
                "score": 0
            }
        ]



def test_feedback_learning_service():

    service = FeedbackLearningService(
        storage=FakeStorage()
    )


    weights = {
        "momentum": 0.5,
        "trend": 0.5
    }


    result = service.learn(
        weights
    )


    assert abs(
        sum(result.values()) - 1
    ) < 0.0001


    assert (
        result["momentum"] > 0
    )