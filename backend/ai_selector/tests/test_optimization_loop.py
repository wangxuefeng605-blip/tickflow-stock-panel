from core.optimization.optimization_loop import (
    OptimizationLoop
)


def test_optimization_loop():

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
            }
        ]
    )


    assert result["strategy"] == "trend"

    assert result["rank"] == 1