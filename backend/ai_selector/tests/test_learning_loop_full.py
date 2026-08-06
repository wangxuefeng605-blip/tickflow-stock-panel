def test_learning_changes_weight():

    weights = get_ai_weights()

    assert "momentum" in weights
    assert "trend" in weights

    assert sum(weights.values()) == 1