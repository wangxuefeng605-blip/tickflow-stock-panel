from core.learning.runtime_service import (
    LearningRuntimeService
)


def test_daily_selector_learning_integration():

    service = LearningRuntimeService()


    result = service.process_daily(
        [
            {
                "code":"000001",
                "score":100
            },
            {
                "code":"000002",
                "score":80
            }
        ],
        "2026-08-07"
    )


    assert len(result) > 0