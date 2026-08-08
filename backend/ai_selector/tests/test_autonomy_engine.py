from core.autonomy.autonomy_engine import AutonomyEngine


def test_autonomy_engine():

    engine = AutonomyEngine()


    result = engine.run_cycle()


    assert result["cycle"] == 1

    assert result["generation"] == 1

    assert result["status"] == "SUCCESS"


    assert result["learning_score"] > 0
    assert result["adaptation_score"] > 0
    assert result["evolution_score"] > 0