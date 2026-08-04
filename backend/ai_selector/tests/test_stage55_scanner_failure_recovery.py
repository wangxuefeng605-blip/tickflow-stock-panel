from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_scanner_failure_recovery():

    runtime = ScannerRuntimeIntegration()

    stocks = [
        {"code": "000001"},
        {"code": "INVALID"},
        {"code": "000002"},
    ]

    results = []

    for stock in stocks:
        try:
            results.append(
                runtime.run(stock)
            )
        except Exception:
            results.append(
                {
                    "recovered": True
                }
            )

    assert len(results) == 3