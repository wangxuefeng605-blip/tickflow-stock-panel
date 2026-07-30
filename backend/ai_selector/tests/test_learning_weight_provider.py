from core.learning.weight_provider import LearningWeightProvider


def test_learning_weight_provider():

    provider = LearningWeightProvider(
        {
            "momentum":0.8
        }
    )


    result = provider.get_weight(
        "momentum"
    )


    assert result == 0.8