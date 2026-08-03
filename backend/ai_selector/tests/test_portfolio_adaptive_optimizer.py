from core.portfolio.adaptive_optimizer import (
    PortfolioAdaptiveOptimizer
)


def test_portfolio_adaptive_optimizer():

    engine = PortfolioAdaptiveOptimizer()


    result = engine.optimize(
        {
            "return":0.2,
            "max_drawdown":0.05
        }
    )


    assert result["portfolio_weight"] > 1
    assert result["risk_adjustment"] < 1