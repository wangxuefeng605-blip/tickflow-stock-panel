from core.runtime_strategy_recovery_decision_risk_analyzer import (
    RuntimeStrategyRecoveryDecisionRiskAnalyzer
)


def test_runtime_strategy_risk_calculation():

    analyzer = (
        RuntimeStrategyRecoveryDecisionRiskAnalyzer()
    )


    result = analyzer.analyze(
        {
            "selected_policy": "restore",
            "confidence": 0.8
        }
    )


    assert result["policy"] == "restore"
    assert result["risk"] == 0.2
    assert result["risk_level"] == "LOW"



def test_runtime_strategy_high_risk():

    analyzer = (
        RuntimeStrategyRecoveryDecisionRiskAnalyzer()
    )


    result = analyzer.analyze(
        {
            "selected_policy": "rollback",
            "confidence": 0.1
        }
    )


    assert result["risk_level"] == "HIGH"



def test_runtime_strategy_risk_history():

    analyzer = (
        RuntimeStrategyRecoveryDecisionRiskAnalyzer()
    )


    analyzer.analyze(
        {
            "selected_policy": "fallback",
            "confidence": 0.5
        }
    )


    assert len(
        analyzer.get_history()
    ) == 1