from core.learning.adaptive_runtime import (
    AdaptiveRuntime
)


def test_adaptive_runtime():

    runtime = AdaptiveRuntime()


    result = (
        runtime.update_weights()
    )


    assert isinstance(
        result,
        dict
    )