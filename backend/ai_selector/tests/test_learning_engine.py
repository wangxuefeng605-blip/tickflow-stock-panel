from core.learning import FeedbackEngine



def test_learning_engine():

    feedback = FeedbackEngine()

    feedback.record(
        {
            "score":1.2,
            "profit":0.05
        }
    )


    result = feedback.learn()


    assert result["samples"] == 1