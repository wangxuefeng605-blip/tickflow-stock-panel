from core.autonomy.autonomy_state import AutonomyState


def test_autonomy_state():

    state = AutonomyState()

    state.next_cycle()

    state.update(
        learning_score=0.8,
        adaptation_score=0.7,
        evolution_score=0.6
    )

    state.complete()

    result = state.snapshot()

    assert result["cycle"] == 1
    assert result["status"] == "SUCCESS"

    assert result["learning_score"] == 0.8
    assert result["adaptation_score"] == 0.7
    assert result["evolution_score"] == 0.6