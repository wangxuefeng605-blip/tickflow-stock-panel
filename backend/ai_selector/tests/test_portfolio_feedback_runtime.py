from core.portfolio.feedback import PortfolioFeedback


def test_portfolio_feedback_runtime():

    engine = PortfolioFeedback()

    result = engine.process(
        [
            {
                "contribution":0.05,
                "drivers":[
                    "momentum"
                ]
            }
        ]
    )


    assert result["feedback"] is True

    assert "momentum" in result["drivers"]