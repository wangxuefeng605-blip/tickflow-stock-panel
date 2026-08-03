from core.portfolio.portfolio_orchestrator import PortfolioOrchestrator


def test_portfolio_orchestrator():

    orchestrator = PortfolioOrchestrator()


    result = orchestrator.run(
        "BULL",
        {
            "reward":0.8,
            "risk":0.1
        }
    )


    assert result["decision"]["action"] == "BUY"

    assert result["learning"] is True