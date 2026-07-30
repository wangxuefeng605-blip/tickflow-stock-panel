from core.learning.pipeline import LearningPipeline


def test_learning_pipeline_update():

    pipeline = LearningPipeline()

    result = pipeline.update(
        feedback={
            "signal":{
                "momentum":0.05
            }
        },
        weights={
            "momentum":0.3
        }
    )

    assert result["updated"] is True