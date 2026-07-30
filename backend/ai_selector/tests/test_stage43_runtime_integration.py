from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_runtime_integration():

    runtime = ScannerRuntimeIntegration()

    result = runtime.run()

    assert result["runtime_ready"] is True