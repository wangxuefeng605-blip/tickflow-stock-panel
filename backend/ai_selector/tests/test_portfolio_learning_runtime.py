from core.portfolio.learning_runtime import PortfolioLearningRuntime


def test_portfolio_learning_runtime():

    runtime = PortfolioLearningRuntime()


    record = runtime.record(
        {
            "action":"BUY",
            "allocation":0.2
        },
        {
            "return":0.1,
            "success":True
        }
    )


    assert "decision" in record
    assert "outcome" in record


    signal = runtime.learn(
        {
            "success":True
        }
    )


    assert signal["reward"] == 1