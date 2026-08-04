import time

from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_scanner_load_test():

    runtime = ScannerRuntimeIntegration()

    stocks = [
        {"code": f"{i:06d}", "momentum": 0.8}
        for i in range(10)
    ]

    start = time.time()

    results = [
        runtime.run(stock)
        for stock in stocks
    ]

    elapsed = time.time() - start

    assert len(results) == 10

    for result in results:
        assert result["runtime_ready"] is True
        assert result["worker_execution_completed"] is True

    assert elapsed < 5