from core.deployment.strategy_registry import StrategyRegistry
from core.deployment.strategy_deployer import StrategyDeployer
from core.policy.policy_state import PolicyState


def test_strategy_deployer():

    registry = StrategyRegistry()

    deployer = StrategyDeployer(
        registry
    )


    policy = PolicyState(
        version="v2",
        score=0.95
    )


    result = deployer.deploy(
        policy
    )


    assert result == policy
    assert registry.active == policy