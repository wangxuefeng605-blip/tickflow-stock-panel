from core.learning.performance_tracker import PerformanceTracker


def test_performance_tracker():

    tracker = PerformanceTracker()


    result = tracker.evaluate(
        {
            "code":"000001",
            "score":0.5
        }
    )


    assert "status" in result