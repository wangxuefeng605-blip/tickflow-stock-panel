from core.runtime_strategy_parameter_tuner import (
    RuntimeStrategyParameterTuner
)


def test_runtime_strategy_parameter_tuner():

    tuner = RuntimeStrategyParameterTuner()

    result = tuner.tune(
        {
            "momentum_weight":0.05
        }
    )

    assert result["tuned"] is True
    assert result["parameters"]["momentum_weight"] == 0.05