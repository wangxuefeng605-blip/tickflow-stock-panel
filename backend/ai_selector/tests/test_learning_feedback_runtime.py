from core.learning.learning_pipeline import LearningPipeline


def test_learning_feedback_runtime():


    pipeline = LearningPipeline()


    result = pipeline.process_feedback(
        [
            {
                "code":"000001",
                "success":True,
                "return_5d":0.08
            }
        ],
        {
            "momentum":0.35
        }
    )


    assert "weights" in result

    assert "learning" in result