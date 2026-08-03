from core.learning.weight_adjuster import (
    WeightAdjuster
)


def test_weight_adjuster():

    adjuster = WeightAdjuster()


    feedback = {

        "signals": {

            "momentum": 0.8,

            "trend": 0.5,

            "risk": 0.2

        }

    }


    result = adjuster.adjust(
        feedback
    )


    assert (
        "momentum"
        in result
    )


    assert (
        result["momentum"]
        >
        0
    )


    assert (
        result["risk"]
        <
        0
    )