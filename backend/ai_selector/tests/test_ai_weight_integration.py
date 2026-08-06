from core.score import alpha_score
from core.ai_weight_provider import get_ai_weights


def test_ai_weight_loaded():

    weights=get_ai_weights()

    assert weights["momentum"]==0.35


def test_score_use_ai_weight():

    score=alpha_score(
        {
            "momentum":1
        }
    )

    assert score==0.35