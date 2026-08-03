from core.portfolio.intelligence_runtime import (
    PortfolioIntelligenceRuntime
)


def test_portfolio_runtime():

    runtime = PortfolioIntelligenceRuntime()


    result = runtime.execute(
        market="BULL",
        signals={
            "reward":0.9,
            "risk":0.1
        }
    )


    assert result["learning"] is True

    assert "strategy" in result

    assert "decision" in result