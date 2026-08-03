from core.execution.risk_checker import RiskChecker


def test_risk_pass():

    checker = RiskChecker()

    decision = {
        "confidence": 0.8,
        "risk": 0.2
    }

    result = checker.check(decision)

    assert result is True