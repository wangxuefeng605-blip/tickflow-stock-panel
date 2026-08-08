from core.deployment.strategy_registry import StrategyRegistry
from core.policy.policy_state import PolicyState


def test_strategy_registry():

    registry = StrategyRegistry()


    policy = PolicyState(
        version="v1",
        score=0.9
    )


    registry.register_candidate(
        policy
    )


    assert len(
        registry.candidates
    ) == 1


    registry.activate(
        policy
    )


    assert registry.get_active() == policy