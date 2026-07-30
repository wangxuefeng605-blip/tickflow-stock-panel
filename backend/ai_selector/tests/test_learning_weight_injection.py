from core.learning.weight_provider import inject_weights


def test_learning_weight_override():

    base={
        "momentum":0.3
    }

    learned={
        "momentum":0.6
    }

    result = inject_weights(
        base,
        learned
    )

    assert result["momentum"] == 0.6