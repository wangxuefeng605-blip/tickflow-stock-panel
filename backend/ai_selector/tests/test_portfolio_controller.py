from core.portfolio.portfolio_controller import PortfolioController


def test_portfolio_controller():

    controller = PortfolioController()


    result = controller.build(
        {
            "capital":100000,
            "signals":
            {
                "000001":0.8,
                "000002":0.4
            }
        }
    )


    assert result["risk"] == "LOW"

    assert result["allocation"]["000001"] > 0