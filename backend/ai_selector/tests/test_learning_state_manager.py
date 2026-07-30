from core.learning.state_manager import LearningStateManager



def test_learning_state_update():


    manager = LearningStateManager()


    manager.update_reward(
        1
    )


    manager.update_weight(
        "momentum",
        0.35
    )


    snapshot = manager.snapshot()


    assert snapshot["rewards"] == [1]

    assert snapshot["weights"]["momentum"] == 0.35