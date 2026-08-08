from core.evolution.policy_mutation import PolicyMutation
from core.policy.policy_state import PolicyState


def test_policy_mutation():

    policy = PolicyState(
        version="v1",
        score=0.8
    )

    mutation = PolicyMutation()

    new_policy = mutation.mutate(
        policy
    )

    assert new_policy.version == "v1-mutated"
    assert new_policy.score == 0.8