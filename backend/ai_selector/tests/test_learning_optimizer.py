from core.learning.optimizer import LearningOptimizer


def test_optimizer_positive_reward():

    optimizer = LearningOptimizer()

    result = optimizer.optimize(
        {
            "reward": 1
        }
    )

    assert result["momentum"] > 1