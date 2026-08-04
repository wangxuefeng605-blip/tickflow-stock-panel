from core.runtime.portfolio_runtime_bridge import PortfolioRuntimeBridge


def test_portfolio_runtime_bridge():

    bridge = PortfolioRuntimeBridge()

    result = bridge.process(
        {
            "reward":1,
            "performance":{
                "return":0.2
            }
        }
    )

    assert result["adjustment"] == "increase"