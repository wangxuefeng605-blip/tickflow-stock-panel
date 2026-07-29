from core.learning.feedback import (
    FeedbackEngine
)

from core.backtest.learning import (
    LearningSignal
)



def test_feedback_generate():

    signal = LearningSignal(

        strategy="AI",

        return_rate=0.1,

        max_drawdown=0.02,

        win_rate=0.6,

        score=0.08

    )


    event = FeedbackEngine().generate(
        signal
    )


    assert event.strategy == "AI"

    assert event.adjustment == 0.08