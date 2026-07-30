from core.learning.ranking_adapter import LearningRankingAdapter


def test_learning_changes_ranking():

    adapter = LearningRankingAdapter()

    factors = {
        "momentum": 1
    }

    weights = {
        "momentum": 2
    }

    result = adapter.apply(
        factors,
        weights
    )

    assert result["momentum"] == 2