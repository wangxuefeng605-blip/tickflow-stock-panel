from core.learning.weight_guard import WeightGuard



def test_weight_guard_limit():

    guard = WeightGuard(
        max_delta=0.05
    )


    current = {

        "momentum":0.35,

        "trend":0.30,

        "quality":0.15,

        "liquidity":0.10,

        "risk":0.10

    }


    proposed = {

        "momentum":0.80,

        "trend":0.05,

        "quality":0.05,

        "liquidity":0.05,

        "risk":0.05

    }


    result = guard.apply(
        current,
        proposed
    )


    assert result["momentum"] <= 0.40

    assert abs(
        sum(result.values())
        -
        1
    ) < 0.001