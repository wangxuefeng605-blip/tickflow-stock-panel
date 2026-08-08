from core.learning.learning_state import LearningState



def test_learning_state():


    state = LearningState()


    state.add_experience(
        {
            "action":"BUY",
            "reward":10
        }
    )


    state.update_reward(
        10
    )


    result = state.snapshot()


    assert result["experience_count"] == 1

    assert result["reward"] == 10

    assert result["version"] == 1