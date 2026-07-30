from core.scanner.runtime_facade import ScannerRuntimeFacade


facade = ScannerRuntimeFacade()


def test_runtime_facade():
    assert facade is not None