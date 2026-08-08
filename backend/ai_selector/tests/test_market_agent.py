from core.agent_runtime.market_agent import MarketAgent


def test_market_agent():

    agent = MarketAgent()

    result = agent.run(
        {
            "market": "BULL"
        }
    )

    assert result["signal"] == "positive"