from core.portfolio import PortfolioOptimizer


def test_portfolio_optimizer():


    optimizer = PortfolioOptimizer()


    result = optimizer.optimize(

        {
            "positions":[
                {
                    "code":"603580",
                    "weight":0.2,
                    "score":0.85
                }
            ]
        },

        {
            "level":"LOW"
        },

        "BULL"

    )


    assert "allocation" in result

    assert "confidence" in result

    assert result["allocation"]["603580"] == 0.35