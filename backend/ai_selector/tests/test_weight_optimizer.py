from core.learning.weight_optimizer import (
    WeightOptimizer
)


from core.learning.feedback import (
    FeedbackEvent
)



def test_weight_update():

    weights = {

        "momentum":0.2,

        "trend":0.3

    }


    feedback = FeedbackEvent(

        strategy="AI",

        score=0.1,

        adjustment=0.1

    )


    result = WeightOptimizer().update(
        weights,
        feedback
    )


    assert result["momentum"] == 0.22

    assert result["trend"] == 0.33