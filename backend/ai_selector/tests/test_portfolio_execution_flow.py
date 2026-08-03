from core.portfolio.portfolio import Portfolio
from core.portfolio.execution_bridge import ExecutionPortfolioBridge


def test_execution_to_portfolio():

    portfolio = Portfolio()


    bridge = ExecutionPortfolioBridge(
        portfolio
    )


    order = {

        "code":"000001",

        "action":"BUY",

        "price":10,

        "qty":100
    }


    state = bridge.process(
        order
    )


    assert "000001" in state["positions"]

    assert state["cash"] == 99000