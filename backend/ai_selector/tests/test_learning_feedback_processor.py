from core.meta_learning.learning_feedback_processor import (
    LearningFeedbackProcessor
)


def test_feedback_process():

    processor = LearningFeedbackProcessor()


    result = processor.process(
        {
            "factor":"momentum",
            "reward":1
        },
        {
            "momentum":0.3
        }
    )


    assert result["momentum"] > 0.3