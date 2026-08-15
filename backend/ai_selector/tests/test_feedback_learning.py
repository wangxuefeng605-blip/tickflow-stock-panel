from core.feedback.evaluator import FeedbackEvaluator

def test_feedback_learning():

    evaluator = FeedbackEvaluator()

    result = evaluator.evaluate(
        [
          {"result":True},
          {"result":False},
          {"result":True}
        ]
    )

    assert result["score"] == 2/3