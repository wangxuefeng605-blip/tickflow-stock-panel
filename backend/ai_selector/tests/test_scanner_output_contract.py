from core.scanner.worker import ScanWorker
from core.intelligence.context import AIContext


def test_scan_worker_ai_output_contract():

    context = AIContext(
        market_state="BULL",
        weights={
            "momentum":0.35,
            "trend":0.30
        },
        confidence=0.9
    )


    worker = ScanWorker(
        "000001",
        context=context
    )


    result = worker.scan()


    if result is not None:

        assert "code" in result

        assert "score" in result

        assert "signals" in result

        assert "market_state" in result

        assert "confidence" in result

        assert "explanation" in result