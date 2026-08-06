from core.learning.performance_evaluator import (
    PerformanceEvaluator
)


def test_evaluate():

    evaluator = PerformanceEvaluator()

    data = [
        {
            "code": "000001",
            "score": 90,
            "return": 0.1
        },
        {
            "code": "000002",
            "score": 80,
            "return": -0.05
        }
    ]

    result = evaluator.evaluate(data)

    assert result["total"] == 2
    assert result["success"] == 1
    assert result["success_rate"] == 0.5