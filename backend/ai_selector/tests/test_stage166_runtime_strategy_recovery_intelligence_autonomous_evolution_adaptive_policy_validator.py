from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_policy_validator import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptivePolicyValidator
)



def test_policy_validation_success():

    validator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptivePolicyValidator()
    )


    result = validator.validate(
        {
            "strategy": "adaptive_restore",
            "confidence_threshold": 0.8,
            "risk_limit": 0.2
        }
    )


    assert result["valid"] is True
    assert result["execution_allowed"] is True



def test_policy_validation_missing_strategy():

    validator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptivePolicyValidator()
    )


    result = validator.validate(
        {
            "confidence_threshold": 0.8,
            "risk_limit": 0.2
        }
    )


    assert result["valid"] is False



def test_policy_validation_high_risk():

    validator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptivePolicyValidator()
    )


    result = validator.validate(
        {
            "strategy": "rollback",
            "confidence_threshold": 0.8,
            "risk_limit": 2
        }
    )


    assert result["execution_allowed"] is False



def test_policy_validation_history():

    validator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptivePolicyValidator()
    )


    validator.validate(
        {
            "strategy": "test",
            "confidence_threshold": 0.5,
            "risk_limit": 0.5
        }
    )


    assert len(
        validator.get_history()
    ) == 1