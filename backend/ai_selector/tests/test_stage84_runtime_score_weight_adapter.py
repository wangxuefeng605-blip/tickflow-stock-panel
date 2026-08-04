from core.runtime_score_weight_adapter import RuntimeScoreWeightAdapter


def test_runtime_score_weight_adapter():

    adapter = RuntimeScoreWeightAdapter()


    result = adapter.apply(
        {
            "weight":0.8
        }
    )


    assert result["momentum"] == 0.8

    assert adapter.current()["trend"] == 0.8