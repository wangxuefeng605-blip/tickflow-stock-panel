from core.learning.portfolio_bridge import (
    PortfolioLearningBridge
)


def test_portfolio_learning_bridge():

    bridge = PortfolioLearningBridge()


    result = bridge.learn(
        {
            "reward":0.2
        }
    )


    assert result["momentum"] > 1
