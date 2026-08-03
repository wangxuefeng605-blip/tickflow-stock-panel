from core.learning.weight_provider import (
    LearningWeightProvider
)


def test_learning_weight_adjustment():


    provider = LearningWeightProvider(
        {
            "momentum":0.35,
            "trend":0.30,
            "quality":0.15,
            "liquidity":0.10,
            "risk":0.10
        }
    )


    result = provider.apply_adjustment(
        {
            "momentum":0.02,
            "risk":-0.02
        }
    )


    assert (
        result["momentum"]
        >
        0.35
    )


    assert (
        result["risk"]
        <
        0.10
    )


    assert (
        round(
            sum(result.values()),
            5
        )
        ==
        1
    )