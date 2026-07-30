from core.learning.optimizer import LearningOptimizer
from core.learning.weight_provider import WeightProvider


def test_learning_updates_weight():

    optimizer = LearningOptimizer()

    result = optimizer.optimize(
        {
            "reward":1
        }
    )

    provider = WeightProvider()