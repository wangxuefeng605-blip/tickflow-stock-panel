from core.learning import LearningRuntimeService

def test_daily_learning_runtime():

    service = LearningRuntimeService()


    result = service.process_daily(
        [
            {
                "code":"000001",
                "score":100
            }
        ],
        "2026-08-07"
    )


    assert result