from core.policy.policy_state import PolicyState
from core.policy.policy_selector import PolicySelector


def test_policy_selector():

    policies = [
        PolicyState(
            version="v1",
            score=0.5
        ),
        PolicyState(
            version="v2",
            score=0.9
        )
    ]

    selector = PolicySelector()

    result = selector.select(
        policies
    )

    assert result.version == "v2"