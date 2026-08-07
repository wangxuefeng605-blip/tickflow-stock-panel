from core.learning import LearningRuntimeService


def test_learning_runtime_service():

    service = LearningRuntimeService()


    paths = service.record_prediction(
        [
            {
                "code":"000001",
                "score":100
            }
        ],
        "2026-08-07"
    )


    assert len(paths)>0