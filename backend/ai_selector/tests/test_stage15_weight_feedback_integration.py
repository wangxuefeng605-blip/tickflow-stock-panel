from core.learning.feedback_loop_runtime import FeedbackLoopRuntime


def test_weight_feedback_integration():

    runtime = FeedbackLoopRuntime()

    result = {
        "profit": 20,
        "factor": "momentum"
    }

    runtime.process(result)

    weights = runtime.state_manager.snapshot()["weights"]

    assert "momentum" in weights