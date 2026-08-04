from core.portfolio.feedback_runtime import PortfolioFeedbackRuntime


def test_portfolio_feedback_runtime():

    runtime = PortfolioFeedbackRuntime()


    result = runtime.run(
        {
            "return":0.2
        }
    )


    assert result is not None