from core.learning.adaptive_weight import AdaptiveWeightEngine


def test_positive_feedback_updates_weight():

    engine = AdaptiveWeightEngine()

    before = engine.weights["momentum"]

    result = engine.adjust(
        "momentum",
        1
    )

    assert result["momentum"] > before



def test_negative_feedback_updates_weight():

    engine = AdaptiveWeightEngine()

    before = engine.weights["momentum"]

    result = engine.adjust(
        "momentum",
        -1
    )

    assert result["momentum"] < before