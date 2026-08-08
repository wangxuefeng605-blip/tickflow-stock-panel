from core.evolution.evolution_history import EvolutionHistory
from core.policy.policy_state import PolicyState


def test_evolution_history():

    history = EvolutionHistory()

    policy = PolicyState(
        version="v1",
        score=0.8
    )

    history.add(
        1,
        policy
    )

    result = history.latest()

    assert result["generation"] == 1
    assert result["policy"] == "v1"
    assert result["score"] == 0.8