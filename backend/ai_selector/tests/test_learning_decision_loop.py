from core.learning.decision_loop import LearningDecisionLoop



def test_learning_decision_loop_updates():


    loop = LearningDecisionLoop()


    result = loop.process(
        {
            "factor": "momentum",
            "reward": 1
        }
    )


    assert result["learning_updated"] is True

    assert result["weights"]["momentum"] > 0.2