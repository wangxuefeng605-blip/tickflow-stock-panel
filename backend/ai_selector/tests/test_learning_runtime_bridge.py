from core.learning.learning_runtime_bridge import LearningRuntimeBridge


def test_learning_runtime_bridge():

    bridge = LearningRuntimeBridge()

    result = bridge.process_feedback(
        "momentum",
        100,
        110
    )

    assert result["success"]