from core.learning.learning_orchestrator import LearningOrchestrator


def test_learning_orchestrator_runtime():

    orchestrator = LearningOrchestrator()


    prediction = orchestrator.record_prediction(
        [
            {
                "code":"000001",
                "score":100
            }
        ],
        "2026-08-07"
    )


    assert len(prediction)>0