from core.learning.ranking_feedback import (
    RankingFeedback
)



def test_ranking_feedback():


    engine = RankingFeedback()


    result = engine.record_prediction(
        [
            {
                "code":"000001",
                "score":100
            }
        ],
        "2026-08-07"
    )


    assert result["date"] == "2026-08-07"


    rewards = engine.evaluate(
        [
            {
                "code":"000001",
                "return":0.05
            }
        ]
    )


    assert rewards[0]["reward"] == 1