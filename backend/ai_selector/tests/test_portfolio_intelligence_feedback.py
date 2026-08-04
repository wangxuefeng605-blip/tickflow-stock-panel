from core.portfolio.intelligence_runtime import PortfolioIntelligenceRuntime


def test_portfolio_intelligence_feedback():

    runtime = PortfolioIntelligenceRuntime()

    result = runtime.run(
        {
            "reward": 1,
            "performance": {
                "return": 0.2
            }
        }
    )

    assert result["adjustment"] == "increase"