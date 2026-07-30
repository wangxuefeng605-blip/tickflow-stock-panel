from core.learning.runtime import LearningRuntime


def test_learning_runtime_updates_weight():

    runtime = LearningRuntime()

    result = runtime.learn(
        {
            "reward": 1,
            "factor": "momentum"
        }
    )

    assert result["momentum"] > 1