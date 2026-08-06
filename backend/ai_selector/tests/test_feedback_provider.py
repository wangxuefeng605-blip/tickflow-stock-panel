from core.learning.feedback_provider import (
    FeedbackProvider
)


def test_provider():

    provider = FeedbackProvider()

    result = provider.load()

    assert isinstance(
        result,
        list
    )