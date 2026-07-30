from core.orchestrator.pipeline import AIOrchestrator


def test_orchestrator_triggers_learning():

    pipeline = AIOrchestrator()

    result = pipeline.run(
        {}
    )

    assert result.learning_updated is True