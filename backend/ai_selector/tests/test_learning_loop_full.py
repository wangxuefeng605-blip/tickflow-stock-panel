from core.ai_weight_provider import get_ai_weights


def test_learning_changes_weight():

    weights = get_ai_weights()

    assert weights

    assert "momentum" in weights

    assert "trend" in weights