from core.autonomy.autonomy_runtime import AutonomyRuntime


def test_autonomy_runtime():

    runtime = AutonomyRuntime()


    result = runtime.run()


    assert result["runtime"] == "ACTIVE"


    assert result["result"]["status"] == "SUCCESS"