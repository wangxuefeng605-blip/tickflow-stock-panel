from core.orchestrator.pipeline import AIOrchestrator


def test_orchestrator_backtest():

    engine = AIOrchestrator()


    result = engine.run(
        "BULL"
    )


    assert result.backtest is not None