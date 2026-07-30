from core.scanner.runtime_bootstrap import ScannerRuntimeBootstrap


def test_runtime_bootstrap():

    bootstrap = ScannerRuntimeBootstrap()

    result = bootstrap.start()

    assert result["status"] == "ready"