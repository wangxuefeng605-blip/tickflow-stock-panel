from core.policy.policy_state import PolicyState


def test_policy_state():

    policy = PolicyState()

    data = policy.snapshot()

    assert data["version"] == "v1"
    assert "momentum" in data["weights"]
    assert data["active"] is True


def test_policy_update():

    policy = PolicyState()

    policy.update_score(0.85)

    assert policy.score == 0.85