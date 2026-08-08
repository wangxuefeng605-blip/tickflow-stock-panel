from core.deployment.strategy_registry import StrategyRegistry
from core.deployment.runtime_policy_switcher import RuntimePolicySwitcher
from core.policy.policy_state import PolicyState


def test_runtime_policy_switcher():

    registry = StrategyRegistry()

    switcher = RuntimePolicySwitcher(
        registry
    )


    policy = PolicyState(
        version="runtime-v1",
        score=0.95
    )


    result = switcher.switch(
        policy
    )


    assert result == policy

    assert switcher.current() == policy