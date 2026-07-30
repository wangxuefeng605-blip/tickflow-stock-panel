from core.learning.decision_ranking_bridge import LearningRankingBridge


def test_learning_ranking_bridge():

    bridge = LearningRankingBridge()

    result = bridge.process(
        {
            "score": 0.8,
            "momentum": 0.9
        },
        {
            "weights": {
                "momentum": 1.2
            }
        }
    )

    assert result["learning_applied"]