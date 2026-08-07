from core.portfolio.portfolio_state import PortfolioState


def test_portfolio_state():

    portfolio = PortfolioState(
        cash=100000
    )


    portfolio.add_position(
        "000001",
        shares=1000,
        cost=10
    )


    assert portfolio.cash == 100000

    assert "000001" in portfolio.positions

    assert portfolio.positions["000001"]["shares"] == 1000

    assert portfolio.total_cost() == 10000