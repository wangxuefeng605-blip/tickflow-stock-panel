from core.learning.weight_adapter import (
    WeightAdapter
)


def test_weight_adjustment():

    adapter = WeightAdapter()


    weights = {
        "momentum":0.35,
        "trend":0.30,
        "quality":0.15,
        "liquidity":0.10,
        "risk":0.10
    }


    signals = {
        "momentum":0.03,
        "risk":0.02
    }


    result = adapter.apply(
        weights,
        signals
    )


    assert result["momentum"] > 0.35
    assert result["risk"] > 0.10

    # 权重归一化
    assert abs(
        sum(result.values()) - 1
    ) < 0.000001