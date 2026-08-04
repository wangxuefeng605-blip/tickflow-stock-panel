import time

from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_scanner_stress_test():

    runtime = ScannerRuntimeIntegration()

    stocks = [
        {
            "code": f"{i:06d}",
            "momentum": 0.8
        }
        for i in range(100)
    ]

    start = time.time()

    results = []

    for stock in stocks:
        results.append(
            runtime.run(stock)
        )

    elapsed = time.time() - start

    assert len(results) == 100

    for result in results:
        assert result["runtime_ready"] is True
        assert result["worker_execution_completed"] is True

    assert elapsed < 10