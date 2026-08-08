from core.evolution.evolution_engine import EvolutionEngine
from core.policy.policy_state import PolicyState


def test_evolution_engine():

    engine = EvolutionEngine()


    a = PolicyState(
        version="v1",
        score=0.8
    )

    b = PolicyState(
        version="v2",
        score=0.9
    )


    result = engine.evolve(
        a,
        b
    )


    assert result.version == "v1-mutated-v2-child"
    assert result.score == 0.9

    assert len(
        engine.history.records
    ) == 1