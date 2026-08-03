from core.portfolio.risk import PortfolioRisk


def test_risk_score():

    risk = PortfolioRisk()


    result = risk.evaluate({})


    assert "risk_score" in result

    assert "status" in result