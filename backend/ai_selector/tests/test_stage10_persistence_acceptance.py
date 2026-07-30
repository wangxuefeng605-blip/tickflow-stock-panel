from core.learning.persistence import LearningPersistence


def test_stage10_learning_state_persistence():

    persistence = LearningPersistence()

    state = {
        "weights": {
            "momentum": 1.2,
            "value": 0.8
        }
    }

    persistence.save(state)

    restored = persistence.load()

    assert restored == state