from core.portfolio.orchestrator import PortfolioOrchestrator


def test_portfolio_intelligence_runtime():

    engine = PortfolioOrchestrator()


    result = engine.analyze(

        {
            "performance": {
                "return":0.5
            },

            "attribution":[
                {
                    "drivers":[
                        "momentum"
                    ]
                }
            ]
        }

    )


    assert "risk" in result

    assert "intelligence" in result

    assert result["intelligence"]["portfolio_score"] > 0