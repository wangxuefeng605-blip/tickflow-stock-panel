from core.evolution.policy_crossover import PolicyCrossover
from core.policy.policy_state import PolicyState


def test_policy_crossover():

    a = PolicyState(
        version="v1",
        score=0.8
    )

    b = PolicyState(
        version="v2",
        score=0.9
    )


    crossover = PolicyCrossover()

    child = crossover.crossover(
        a,
        b
    )


    assert child.version == "v1-v2-child"
    assert child.score == 0.9