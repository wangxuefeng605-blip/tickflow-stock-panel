from core.orchestrator.pipeline import AIOrchestrator


def test_orchestrator_portfolio():

    engine = AIOrchestrator()


    result = engine.run(
        market="BULL"
    )


    assert result.portfolio is not None