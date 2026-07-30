from core.orchestrator.pipeline import AIOrchestrator

def test_stage8_full_ai_loop():

    orchestrator = AIOrchestrator()

    context = orchestrator.run(
        {
            "trend":1
        }
    )

    assert context.ranking

    assert context.decision

    assert context.orders

    assert context.learning_updated