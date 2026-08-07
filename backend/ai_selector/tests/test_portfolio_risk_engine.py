from core.portfolio.portfolio_state import PortfolioState
from core.portfolio.portfolio_risk_engine import PortfolioRiskEngine


def test_portfolio_risk_engine():

    portfolio = PortfolioState(
        cash=100000
    )


    portfolio.add_position(
        "000001",
        shares=1000,
        cost=10
    )


    engine = PortfolioRiskEngine()


    result = engine.evaluate(
        portfolio
    )


    assert result["exposure"] == 0.1

    assert result["risk"] == "LOW"