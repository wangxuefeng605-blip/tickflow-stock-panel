from core.evolution.evolution_engine import EvolutionEngine
from core.policy.policy_state import PolicyState


def test_stage46_strategy_evolution():

    engine = EvolutionEngine()

    policy_a = PolicyState(
        version="v1",
        score=0.8
    )

    policy_b = PolicyState(
        version="v2",
        score=0.9
    )


    evolved = engine.evolve(
        policy_a,
        policy_b
    )


    assert evolved.version == "v1-mutated-v2-child"

    assert evolved.score == 0.9

    assert len(
        engine.history.records
    ) == 1