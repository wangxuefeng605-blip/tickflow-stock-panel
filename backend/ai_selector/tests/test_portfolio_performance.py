from core.portfolio.portfolio import Portfolio
from core.portfolio.performance import PortfolioPerformance


def test_performance_calculation():

    portfolio = Portfolio()

    performance = PortfolioPerformance(portfolio)

    result = performance.evaluate()

    assert "return" in result
    assert "drawdown" in result
    assert "score" in result