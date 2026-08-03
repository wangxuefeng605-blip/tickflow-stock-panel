from core.portfolio.portfolio import Portfolio


def test_portfolio_buy():

    portfolio = Portfolio()


    result = portfolio.buy(
        "000001",
        10,
        100
    )


    assert result is True


    assert "000001" in portfolio.positions


    assert portfolio.cash == 99000