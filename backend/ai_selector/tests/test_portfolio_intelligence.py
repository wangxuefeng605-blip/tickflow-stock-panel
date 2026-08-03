from core.portfolio.intelligence import PortfolioIntelligence


def test_portfolio_intelligence():

    engine = PortfolioIntelligence()


    result = engine.analyze(

        {
            "return":0.1
        },

        {
            "risk_score":0.2
        },

        [
            {
                "drivers":[
                    "momentum"
                ]
            }
        ]

    )


    assert result["risk_level"]=="LOW"

    assert "momentum" in result["top_drivers"]
