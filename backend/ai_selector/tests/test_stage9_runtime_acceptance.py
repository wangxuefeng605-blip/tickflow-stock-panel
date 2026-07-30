from core.orchestrator.pipeline import AIOrchestrator


def test_stage9_runtime_full_loop():

    orchestrator = AIOrchestrator()

    result = orchestrator.run(
        "BULL"
    )

    assert result is not None