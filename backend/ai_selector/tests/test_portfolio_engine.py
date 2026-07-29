from core.intelligence.portfolio_engine import PortfolioEngine


def test_portfolio_decision():

    engine = PortfolioEngine()


    result = engine.evaluate(
        {
            "code":"603580",
            "score":0.41,
            "confidence":0.85,
            "signals":[
                "Strong momentum"
            ]
        }
    )


    assert result["action"] in [
        "BUY",
        "HOLD",
        "AVOID"
    ]

    assert "risk" in result