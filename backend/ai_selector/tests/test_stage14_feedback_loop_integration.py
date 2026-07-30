from core.learning.feedback_loop_runtime import FeedbackLoopRuntime


def test_feedback_loop_full_cycle():

    runtime = FeedbackLoopRuntime()

    result = {
        "profit": 10
    }

    runtime.process(result)

    state = runtime.state_manager.snapshot()

    assert len(state["rewards"]) == 1