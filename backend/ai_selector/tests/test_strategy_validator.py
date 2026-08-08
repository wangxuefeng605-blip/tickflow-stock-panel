from core.deployment.strategy_validator import StrategyValidator
from core.policy.policy_state import PolicyState


def test_strategy_validator():

    validator = StrategyValidator()


    good = PolicyState(
        version="v2",
        score=0.9
    )

    bad = PolicyState(
        version="v3",
        score=0.2
    )


    assert validator.validate(
        good
    )


    assert not validator.validate(
        bad
    )