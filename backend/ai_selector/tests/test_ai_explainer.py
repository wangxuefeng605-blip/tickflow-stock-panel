from core.intelligence.explainer import AIExplainer
from core.intelligence.context import AIContext



def test_ai_explanation():


    context = AIContext(
        market_state="BULL",
        weights={
            "momentum":0.35
        },
        confidence=0.9
    )


    factors={
        "momentum":0.8,
        "trend":0.5
    }


    result = (
        AIExplainer()
        .explain(
            factors,
            context
        )
    )


    assert (
        "Strong momentum"
        in result["signals"]
    )


    assert (
        result["market_state"]
        ==
        "BULL"
    )