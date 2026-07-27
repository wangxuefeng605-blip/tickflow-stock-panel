from core.intelligence.weight_engine import WeightEngine


def test_weight_engine():

    engine = WeightEngine()


    bull = engine.get_weights(
        "BULL"
    )


    assert bull["momentum"] == 0.35


    bear = engine.get_weights(
        "BEAR"
    )


    assert bear["quality"] == 0.30