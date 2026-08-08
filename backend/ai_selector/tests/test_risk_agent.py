from core.agent_runtime.risk_agent import RiskAgent


def test_risk_agent():

    agent = RiskAgent()

    result = agent.run(
        {
            "volatility":0.2
        }
    )

    assert result["risk"] == "LOW"