from core.feedback.collector import FeedbackCollector


def test_feedback_collector(tmp_path):

    collector = FeedbackCollector(
        storage=None
    )


    record = collector.collect(
        stock_code="000001",
        prediction="BUY",
        actual_result="WIN",
        score=1
    )


    assert record.stock_code == "000001"