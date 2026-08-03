from core.portfolio.attribution import PortfolioAttribution


def test_attribution():

    engine = PortfolioAttribution()

    result = engine.calculate(
        [
            {
                "code":"603580",
                "return":0.1,
                "weight":0.5,
                "factors":{
                    "momentum":0.9
                }
            }
        ]
    )

    assert result[0]["code"]=="603580"
    assert result[0]["contribution"]==0.05