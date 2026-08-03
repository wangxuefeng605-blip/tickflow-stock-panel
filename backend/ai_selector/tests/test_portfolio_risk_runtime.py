from core.portfolio.portfolio import Portfolio
from core.risk.risk_engine import RiskEngine
from core.runtime.portfolio_runtime import PortfolioRuntime


def test_portfolio_risk_runtime():

    portfolio = Portfolio()

    risk_engine = RiskEngine()

    runtime = PortfolioRuntime(
        portfolio,
        risk_engine
    )


    order = {

        "code": "000001",

        "action": "BUY",

        "price": 10,

        "qty": 100

    }


    state = runtime.execute(
        order
    )


    assert state["status"] == "EXECUTED"


    assert "000001" in state["portfolio"]["positions"]


    assert state["portfolio"]["cash"] == 99000