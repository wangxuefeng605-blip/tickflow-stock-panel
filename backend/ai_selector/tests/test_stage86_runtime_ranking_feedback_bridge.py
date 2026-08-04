from core.runtime_ranking_feedback_bridge import RuntimeRankingFeedbackBridge


def test_runtime_ranking_feedback_bridge():

    bridge = RuntimeRankingFeedbackBridge()

    result = bridge.feedback(
        {
            "rank": 1,
            "score": 95
        }
    )

    assert result["updated"] is True

    assert result["rank"] == 1