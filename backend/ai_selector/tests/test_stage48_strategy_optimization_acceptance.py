from core.optimization.optimization_loop import (
    OptimizationLoop
)


def test_stage48_strategy_optimization():

    loop = OptimizationLoop()


    result = loop.run(
        [
            {
                "strategy": "momentum",
                "score": 0.82
            },
            {
                "strategy": "trend",
                "score": 0.91
            },
            {
                "strategy": "value",
                "score": 0.75
            }
        ]
    )


    assert result is not None

    assert result["strategy"] == "trend"

    assert result["rank"] == 1

    assert result["score"] == 0.91