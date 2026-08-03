from core.portfolio.intelligence import PortfolioIntelligence


def test_portfolio_intelligence():

    engine = PortfolioIntelligence()


    result = engine.analyze(

        performance={
            "return": 0.12
        },

        risk={
            "risk_score": 0.05
        },

        attribution=[

            {
                "drivers":[
                    "momentum",
                    "quality"
                ]
            }

        ]

    )


    assert result["portfolio_score"] > 0

    assert result["risk_level"] == "LOW"

    assert "momentum" in result["top_drivers"]