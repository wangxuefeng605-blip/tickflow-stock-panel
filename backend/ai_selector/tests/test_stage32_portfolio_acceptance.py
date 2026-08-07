from core.portfolio.portfolio_controller import PortfolioController


def test_stage32_full_portfolio_loop():

    controller = PortfolioController()


    result = controller.build(
        {
            "capital":100000,

            "signals":
            {
                "000001":0.9,
                "000002":0.6,
                "000003":0.3
            }
        }
    )


    assert "risk" in result

    assert "allocation" in result

    assert result["allocation"]["000001"] > 0