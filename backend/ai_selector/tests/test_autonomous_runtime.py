from core.runtime.autonomous_runtime import (
    AutonomousRuntime
)


def test_autonomous_runtime_success():

    runtime = AutonomousRuntime()


    runtime.health.update(
        "scanner",
        "ERROR"
    )


    result = runtime.execute(
        "scanner",
        lambda: "RECOVERED",
        "FAILED"
    )


    assert result["status"] in [
        "RECOVERED",
        "SKIPPED"
    ]