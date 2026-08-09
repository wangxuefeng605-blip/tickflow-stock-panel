from core.runtime.intraday_scanner import (
    IntradayScanner
)


def test_intraday_scanner():

    scanner = IntradayScanner()


    result = (
        scanner.run_once()
    )


    assert result is True