from core.meta.meta_optimizer import MetaOptimizer



def test_meta_optimizer():


    optimizer = MetaOptimizer()


    result = optimizer.optimize(
        {
            "momentum": 0.5,
            "trend": 0.3
        },
        0.2
    )


    assert result["optimized"] is True

    assert result["parameters"]["momentum"] == 0.51

    assert result["parameters"]["trend"] == 0.31