from core.learning.adaptive_weight import AdaptiveWeightEngine
from core.learning.weight_optimizer import WeightOptimizer


class Feedback:

    adjustment = 0.1



def test_stage12_adaptive_learning():

    engine = AdaptiveWeightEngine()

    before = engine.weights["momentum"]


    result = engine.adjust(
        "momentum",
        1
    )


    assert (
        result["momentum"]
        > before
    )



def test_weight_optimizer():

    optimizer = WeightOptimizer()


    result = optimizer.update(
        {
            "momentum":1.0
        },
        Feedback()
    )


    assert (
        result["momentum"]
        == 1.1
    )