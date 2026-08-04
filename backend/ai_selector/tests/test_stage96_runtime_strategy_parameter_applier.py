from core.runtime_strategy_parameter_applier import (
    RuntimeStrategyParameterApplier
)


def test_runtime_strategy_parameter_applier():

    applier = RuntimeStrategyParameterApplier()


    result = applier.apply(
        {
            "momentum_weight": 0.05,
            "risk_weight": -0.02
        }
    )


    assert result["applied"] is True

    assert result["parameters"]["momentum_weight"] == 0.05

    assert result["parameters"]["risk_weight"] == -0.02