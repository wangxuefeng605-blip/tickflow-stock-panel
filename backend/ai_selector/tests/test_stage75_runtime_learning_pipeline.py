from core.runtime_learning_pipeline import RuntimeLearningPipeline


def test_runtime_learning_pipeline():

    pipeline = RuntimeLearningPipeline()


    result = pipeline.process(
        {
            "execution_success": True
        }
    )


    assert result["learning_completed"] is True

    assert "memory" in result

    assert "optimization" in result