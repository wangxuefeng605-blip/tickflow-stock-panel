from core.learning.state_manager import LearningStateManager
from core.learning.persistence import LearningPersistence



def test_stage11_state_manager_persistence():


    persistence = LearningPersistence()


    manager = LearningStateManager(
        persistence
    )


    manager.update_weight(
        "momentum",
        1.5
    )


    manager.update_reward(
        0.8
    )


    manager.save()


    restored = LearningStateManager(
        persistence
    )


    restored.load()


    assert (
        restored.snapshot()["weights"]["momentum"]
        == 1.5
    )


    assert (
        restored.snapshot()["rewards"][0]
        == 0.8
    )