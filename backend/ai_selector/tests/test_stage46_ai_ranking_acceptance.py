from core.ranking import rank_stocks


def test_ai_ranking_changes_order():

    results = [
        {
            "code":"AAA",
            "score":0.80,
            "market_state":"BEAR",
            "confidence":1
        },
        {
            "code":"BBB",
            "score":0.75,
            "market_state":"BULL",
            "confidence":1
        }
    ]

    ranked = rank_stocks(results)
