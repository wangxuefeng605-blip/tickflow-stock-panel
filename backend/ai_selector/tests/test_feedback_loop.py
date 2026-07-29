from core.learning.feedback_loop import (
    FeedbackLoop
)

from core.backtest.models import (
    BacktestResult
)



def test_feedback_loop():


    result = BacktestResult(

        total_return=0.1,

        max_drawdown=0.02,

        trades=[],

        strategy="AI"

    )


    weights={

        "momentum":0.2,

        "trend":0.3

    }


    updated = FeedbackLoop().run(
        result,
        weights
    )


    assert updated["momentum"] > 0.2

    assert updated["trend"] > 0.3