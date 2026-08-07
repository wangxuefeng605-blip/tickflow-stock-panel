from core.meta_learning.meta_weight_optimizer import (
    MetaWeightOptimizer
)


def test_weight_update():

    optimizer = MetaWeightOptimizer()


    weights = {
        "momentum":0.3,
        "trend":0.3
    }


    result = optimizer.update(
        weights,
        {
            "factor":"momentum",
            "reward":1
        }
    )


    assert result["momentum"] > 0.3