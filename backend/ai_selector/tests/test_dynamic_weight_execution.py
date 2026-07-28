from core.intelligence.context import AIContext
from core.score import alpha_score


def test_alpha_score_dynamic_weight():

    context = AIContext(

        market_state="BULL",

        weights={

            "momentum":0.8,
            "trend":0.2,
            "quality":0,
            "liquidity":0

        },

        confidence=0.9

    )


    factors={

        "momentum":1,

        "trend":0

    }


    score = alpha_score(

        factors,

        context=context

    )


    assert score == 0.8