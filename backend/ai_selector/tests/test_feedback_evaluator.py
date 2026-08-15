from core.feedback.evaluator import FeedbackEvaluator


def test_feedback_evaluator():


    evaluator = FeedbackEvaluator()


    result = evaluator.evaluate(
        [
            {
                "stock_code":"000001",
                "prediction":"BUY",
                "actual_result":"WIN",
                "score":1
            },
            {
                "stock_code":"000002",
                "prediction":"BUY",
                "actual_result":"LOSS",
                "score":0
            }
        ]
    )


    assert result["count"] == 2
    assert result["success"] == 1
    assert result["accuracy"] == 0.5