from core.policy.policy_registry import PolicyRegistry
from core.policy.policy_state import PolicyState


def test_policy_registry():

    registry = PolicyRegistry()

    policy = PolicyState(
        version="v1"
    )

    registry.register(policy)

    result = registry.get("v1")

    assert result.version == "v1"



def test_active_policy():

    registry = PolicyRegistry()

    policy = PolicyState()

    registry.register(policy)

    active = registry.get_active()

    assert active.active is True