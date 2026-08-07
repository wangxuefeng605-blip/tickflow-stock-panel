from core.learning.runtime_service import (
    LearningRuntimeService
)


def test_ranking_feedback_runtime():

    service = LearningRuntimeService()


    result = service.record_ranking_prediction(
        [
            {
                "code":"000001",
                "score":100
            }
        ],
        "2026-08-07"
    )


    assert result["date"] == "2026-08-07"

    assert len(
        result["ranking"]
    ) == 1