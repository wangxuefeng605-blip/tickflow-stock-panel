from core.runtime_reward_memory import RuntimeRewardMemory


def test_runtime_reward_memory():

    memory = RuntimeRewardMemory()


    result = memory.record(
        {
            "reward":1
        }
    )


    assert result["stored"] is True

    assert memory.latest()["reward"] == 1