from core.deployment.strategy_registry import StrategyRegistry
from core.deployment.strategy_validator import StrategyValidator
from core.deployment.strategy_deployer import StrategyDeployer
from core.deployment.runtime_policy_switcher import RuntimePolicySwitcher
from core.deployment.autonomous_deployment_loop import AutonomousDeploymentLoop
from core.policy.policy_state import PolicyState


def test_autonomous_deployment_loop():

    registry = StrategyRegistry()

    loop = AutonomousDeploymentLoop(
        StrategyValidator(),
        StrategyDeployer(registry),
        RuntimePolicySwitcher(registry)
    )


    policy = PolicyState(
        version="auto-v1",
        score=0.9
    )


    result = loop.deploy(
        policy
    )


    assert result is True

    assert registry.active == policy