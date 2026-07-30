from core.learning.decision_pipeline import LearningDecisionPipeline


def test_learning_decision_pipeline():

    pipeline = LearningDecisionPipeline()


    result = pipeline.process(
        {
            "factor": "momentum",
            "reward": 1
        }
    )


    assert result["learning_updated"] is True
    assert "weights" in result