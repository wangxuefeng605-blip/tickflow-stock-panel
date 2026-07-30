from core.learning.ranking_adapter import LearningRankingAdapter


def test_learning_updates_ranking_weight():

    adapter = LearningRankingAdapter()

    result = adapter.apply_learning(
        {
            "weights": {
                "momentum": 0.3
            }
        },
        {
            "adjustments": {
                "momentum": 0.1
            }
        }
    )

    assert result["weights"]["momentum"] == 0.4
    assert result["learning_applied"] is True