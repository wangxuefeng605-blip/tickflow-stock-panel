from core.runtime_learning_optimizer import RuntimeLearningOptimizer


def test_runtime_learning_optimizer():

    optimizer = RuntimeLearningOptimizer()


    result = optimizer.optimize()


    assert "preferred_mode" in result

    assert "confidence" in result