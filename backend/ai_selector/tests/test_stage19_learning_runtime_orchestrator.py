from core.learning.runtime_orchestrator import LearningRuntimeOrchestrator


def test_learning_runtime_orchestrator():

    orchestrator = LearningRuntimeOrchestrator()


    result = orchestrator.run(
        {
            "code":"000001",
            "momentum":0.8
        }
    )


    assert result["learning_applied"]

    assert "decision" in result