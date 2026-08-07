from core.optimization.adaptive_parameter_tuner import (
    AdaptiveParameterTuner
)



def test_parameter_tuner():


    tuner = AdaptiveParameterTuner()


    result = tuner.update(
        "latency",
        2
    )


    assert (
        result["worker_count"]
        ==
        9
    )


    result = tuner.update(
        "accuracy",
        0.5
    )


    assert (
        result["ranking_weight"]
        ==
        1.1
    )