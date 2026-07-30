from core.learning.memory_manager import LearningMemoryManager



def test_learning_memory_save():


    manager = LearningMemoryManager()


    manager.save(
        {
            "factor":"momentum",
            "reward":1,
            "weight_before":0.2,
            "weight_after":0.35
        }
    )


    records = manager.recent()


    assert len(records) == 1

    assert records[0]["factor"] == "momentum"

    assert records[0]["weight_after"] == 0.35