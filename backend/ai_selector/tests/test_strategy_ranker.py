from core.optimization.strategy_ranker import StrategyRanker


def test_strategy_ranker():

    ranker = StrategyRanker()

    result = ranker.rank(
        [
            {
                "strategy": "momentum",
                "score": 0.82
            },
            {
                "strategy": "trend",
                "score": 0.91
            }
        ]
    )

    assert result[0]["strategy"] == "trend"

    assert result[0]["rank"] == 1