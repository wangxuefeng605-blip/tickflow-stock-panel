from core.learning.adaptive_weight import AdaptiveWeightEngine



def test_positive_reward_increase_weight():

    engine = AdaptiveWeightEngine()


    result = engine.adjust(
        "momentum",
        1
    )


    assert result["momentum"] > 0.2



def test_negative_reward_reduce_weight():

    engine = AdaptiveWeightEngine()


    result = engine.adjust(
        "momentum",
        -1
    )


    assert result["momentum"] < 0.2