from core.orchestrator.pipeline import AIOrchestrator


def test_pipeline():

    engine = AIOrchestrator()

    result = engine.run(
        market="BULL"
    )

    assert result.strategy=="momentum"