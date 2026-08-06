from core.ranking import RankingPipeline
from core.learning import FeedbackEngine


def test_ranking_learning_integration():

    feedback = FeedbackEngine()

    feedback.record(
        {
            "code":"000001",
            "score":90,
            "profit":0.1
        }
    )

    result = feedback.learn()

    assert result["samples"] == 1