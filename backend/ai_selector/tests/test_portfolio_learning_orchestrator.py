from core.portfolio.learning_bridge import PortfolioLearningBridge


def test_portfolio_learning_bridge():

    bridge = PortfolioLearningBridge()


    result = bridge.evaluate(
        {
            "return":0.1
        }
    )


    assert result["reward"] == 1
    assert result["source"] == "portfolio"