from core.intelligence.context import AIContext


def test_scanner_worker_accept_ai_context():

    context = AIContext(
        market_state="BULL",
        weights={
            "momentum": 0.35,
            "trend": 0.30
        },
        confidence=0.9
    )


    # 模拟 ScannerWorker 接收 context
    class MockWorker:


        from core.intelligence.context import AIContext
        from core.scanner.worker import ScanWorker


        def test_scanner_worker_accept_ai_context():


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


            assert worker.context is not None

            assert worker.context.market_state == "BULL"

            assert (
                worker.context.weights["momentum"]
                ==
                0.35
            )