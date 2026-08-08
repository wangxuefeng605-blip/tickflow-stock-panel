from core.autonomy.autonomy_controller import AutonomyController


def test_autonomy_controller():

    controller = AutonomyController()


    result = controller.execute()


    assert result["status"] == "SUCCESS"


    assert "autonomy" in result


    assert result["autonomy"]["cycle"] == 1