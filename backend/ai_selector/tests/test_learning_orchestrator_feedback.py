from core.learning.learning_orchestrator import LearningOrchestrator


def test_learning_orchestrator_feedback():

    orchestrator = LearningOrchestrator()


    result = orchestrator.process_feedback(
        [
            {
                "code":"000001",
                "success":True,
                "return_5d":0.08
            }
        ],
        {
            "momentum":0.35
        }
    )


    assert "weights" in result