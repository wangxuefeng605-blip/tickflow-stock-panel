from core.risk.risk_engine import RiskEngine



def test_risk_engine():


    engine = RiskEngine()



    portfolio = {


        "cash":90000,


        "positions":{


            "000001":{


                "qty":1000,

                "price":10

            }

        }

    }



    result = engine.evaluate(
        portfolio
    )


    assert result["allowed"]


    assert result["risk"] == "LOW"