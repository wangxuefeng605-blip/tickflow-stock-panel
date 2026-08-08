from core.learning.learning_loop import LearningLoop


def test_stage43_agent_learning_loop():

    loop = LearningLoop()


    result = loop.learn(
        {
            "strategy":"momentum",
            "reward":0.9
        }
    )


    assert result["learned"] is True