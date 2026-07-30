from core.learning.pipeline_assembly import LearningPipelineAssembly


def test_learning_pipeline_assembly():

    pipeline = LearningPipelineAssembly()


    result = pipeline.execute(
        {
            "code": "000001",
            "momentum": 0.8
        }
    )


    assert result["pipeline_completed"]

    assert result["learning_applied"]