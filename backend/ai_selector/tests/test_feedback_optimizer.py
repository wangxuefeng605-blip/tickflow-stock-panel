from core.feedback.optimizer import WeightOptimizer

def test_feedback_optimizer():

    optimizer = WeightOptimizer()

    result = optimizer.optimize({
        "score": 0.75,
        "samples": 100,
    })

    assert result["weight"] == 1.0
    assert result["status"] == "UPDATED"