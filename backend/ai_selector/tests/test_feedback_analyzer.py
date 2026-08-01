from core.learning import FeedbackAnalyzer


def test_feedback_analyzer():

    analyzer = FeedbackAnalyzer()

    result = analyzer.analyze(
        {
            "future_return": 0.1,
            "momentum": 0.8
        }
    )

    assert result["momentum"] > 0