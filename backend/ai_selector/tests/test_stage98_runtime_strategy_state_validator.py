from core.runtime_strategy_state_validator import (
    RuntimeStrategyStateValidator
)


def test_runtime_strategy_state_validator():

    validator = RuntimeStrategyStateValidator()

    state = {
        "momentum_weight": 0.35,
        "trend_weight": 0.30,
        "quality_weight": 0.15,
        "liquidity_weight": 0.10,
        "risk_weight": 0.10,
    }

    result = validator.validate(state)

    assert result["valid"] is True


def test_runtime_strategy_state_validator_invalid():

    validator = RuntimeStrategyStateValidator()

    state = {
        "momentum_weight": 1.5
    }

    result = validator.validate(state)

    assert result["valid"] is False