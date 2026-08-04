from core.runtime_strategy_self_healing_validator import (
    RuntimeStrategySelfHealingValidator
)



def test_runtime_strategy_healing_validation_success():

    validator = RuntimeStrategySelfHealingValidator()


    result = validator.validate(
        {
            "status": "healed"
        }
    )


    assert result["valid"] is True
    assert result["health"] == "healthy"



def test_runtime_strategy_healing_validation_failed():

    validator = RuntimeStrategySelfHealingValidator()


    result = validator.validate(
        {
            "status": "rollback"
        }
    )


    assert result["valid"] is False
    assert result["health"] == "degraded"



def test_runtime_strategy_validation_history():

    validator = RuntimeStrategySelfHealingValidator()


    validator.validate(
        {
            "status": "healed"
        }
    )


    assert len(
        validator.validation_history()
    ) == 1