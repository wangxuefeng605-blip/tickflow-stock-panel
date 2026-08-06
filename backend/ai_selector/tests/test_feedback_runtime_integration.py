from core.learning.learning_pipeline import LearningPipeline

from core.learning.learning_pipeline import LearningPipeline


def test_feedback_runtime_integration():

    pipeline = LearningPipeline()

    ...


    result = pipeline.process_feedback(
        [
            {
                "code":"000001",
                "success":True
            }
        ]
    )


    assert result[0]["reward"] == 1