from core.runtime_strategy_learning_feedback_bridge import (
    RuntimeStrategyLearningFeedbackBridge
)


def test_runtime_strategy_learning_feedback_bridge():

    bridge = RuntimeStrategyLearningFeedbackBridge()

    result = bridge.process(
        {
            "reward":0.8
        }
    )

    assert result["processed"] is True
    assert result["feedback"]["reward"] == 0.8