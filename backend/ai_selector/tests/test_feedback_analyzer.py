from core.learning.feedback_analyzer import (
    FeedbackAnalyzer
)


def test_feedback_analyzer():

    analyzer = FeedbackAnalyzer()


    result = analyzer.analyze()


    assert (
        "success_rate"
        in result
    )

    assert (
        "total"
        in result
    )