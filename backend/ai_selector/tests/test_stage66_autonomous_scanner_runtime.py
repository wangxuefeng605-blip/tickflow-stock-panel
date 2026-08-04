from core.autonomous_scanner_runtime import AutonomousScannerRuntime


def test_autonomous_scanner_runtime():

    runtime = AutonomousScannerRuntime()


    result = runtime.run(
        {
            "success_rate":0.98,
            "retry_count":1
        }
    )


    assert result["autonomous"] is True

    assert "scanner_config" in result