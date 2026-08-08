from core.optimization.auto_promotion_engine import (
    AutoPromotionEngine
)


def test_auto_promotion_engine():

    engine = AutoPromotionEngine()


    result = engine.promote(
        [
            {
                "rank": 1,
                "strategy": "trend",
                "score": 0.91
            },
            {
                "rank": 2,
                "strategy": "momentum",
                "score": 0.82
            }
        ]
    )


    assert result["strategy"] == "trend"

    assert engine.get_promoted() == result