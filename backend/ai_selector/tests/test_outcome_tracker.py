from core.learning.outcome.outcome_tracker import (
    OutcomeTracker
)


def test_outcome_tracker():

    tracker = OutcomeTracker()


    path = tracker.save_prediction_outcome(
        code="000001",
        prediction_date="2026-08-03",
        score=90
    )


    assert path.exists()


    tracker.update_result(
        "000001",
        {
            "return_5d":0.08,
            "success":True
        }
    )


    records = tracker.load_all()


    assert len(records) > 0


    item = records[-1]


    assert item["code"] == "000001"

    assert (
        item["result"]["success"]
        is True
    )