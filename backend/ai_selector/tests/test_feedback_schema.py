from core.feedback.schema import FeedbackRecord


def test_feedback_schema():

    record = FeedbackRecord(
        stock_code="000001",
        prediction="BUY",
        actual_result="WIN",
        score=1,
        source="test"
    )


    data = record.to_dict()


    assert data["stock_code"] == "000001"
    assert data["prediction"] == "BUY"
    assert data["score"] == 1


    restored = FeedbackRecord.from_dict(data)


    assert restored.stock_code == "000001"
    assert restored.source == "test"