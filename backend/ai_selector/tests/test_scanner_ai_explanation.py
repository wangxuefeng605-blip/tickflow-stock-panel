from core.scanner.worker import ScanWorker
from core.intelligence.context import AIContext


def test_worker_output_ai_explanation():


    context = AIContext(

        market_state="BULL",

        weights={
            "momentum":0.35
        },

        confidence=0.9
    )


    worker = ScanWorker(
        "000001",
        context=context
    )


    assert worker.context.market_state=="BULL"