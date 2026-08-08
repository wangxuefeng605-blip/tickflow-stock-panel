from core.learning.learning_evaluator import LearningEvaluator



def test_learning_evaluator():


    evaluator = LearningEvaluator()


    result = evaluator.evaluate(
        {
            "decision":{
                "action":"BUY"
            },
            "reward":20
        }
    )


    assert result["score"] == 20

    assert result["reward"] == 20

    assert result["level"] == "POSITIVE"