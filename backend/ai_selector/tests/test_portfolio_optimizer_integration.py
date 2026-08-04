from core.portfolio import PortfolioOrchestrator


def test_portfolio_optimizer_integration():


    engine = PortfolioOrchestrator()


    result = engine.analyze(

        {

            "performance":{
                "return":0.5
            },


            "market_state":"BULL",


            "positions":[

                {
                    "code":"603580",
                    "weight":0.2,
                    "score":0.85
                }

            ],


            "attribution":[

                {
                    "drivers":[
                        "momentum"
                    ]
                }

            ]

        }

    )


    assert "optimization" in result

    assert "allocation" in result["optimization"]