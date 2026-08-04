from core.portfolio.autonomous_runtime import PortfolioAutonomousRuntime

def test_portfolio_autonomous_runtime():

    runtime = PortfolioAutonomousRuntime()

    result = runtime.run(
        {
            "market_state":"BULL",
            "positions":[
                {
                    "code":"603580",
                    "weight":0.2
                }
            ]
        }
    )


    assert "action" in result
    assert "allocation" in result
    assert "risk" in result