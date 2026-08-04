from core.runtime_learning_memory import RuntimeLearningMemory


def test_runtime_learning_memory():

    memory = RuntimeLearningMemory()


    result = memory.store(
        {
            "execution_success":True
        }
    )


    assert result["stored"] is True

    assert result["total_records"] == 1