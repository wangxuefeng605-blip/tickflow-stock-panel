from core.ranking.ranker import Ranker


def test_ranking_contract():

    results = [

        {
            "code": "000001",
            "score": 0.8,

            "signals": [
                "Trend confirmed"
            ],

            "market_state": "BULL",

            "confidence": 0.85,

            "factors": {
                "momentum": 0.8,
                "quality": 0.7
            }
        }

    ]


    ranked = Ranker().rank(
        results
    )


    assert len(ranked) == 1


    item = ranked[0]


    assert item.code == "000001"

    assert item.score == 0.8

    assert item.market_state == "BULL"

    assert item.confidence == 0.85

    assert len(item.signals) > 0

    assert item.ranking_reason