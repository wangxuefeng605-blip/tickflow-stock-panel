from core.runtime_learning_feedback_processor import RuntimeLearningFeedbackProcessor


def test_runtime_learning_feedback_processor():

    processor = RuntimeLearningFeedbackProcessor()


    result = processor.process(
        {
            "score":95
        }
    )


    assert result["processed"] is True

    assert result["reward"] == 1