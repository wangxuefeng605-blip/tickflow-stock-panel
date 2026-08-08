from core.agent.agent_memory import AgentMemory


def test_agent_memory():

    memory = AgentMemory()

    memory.remember(
        {
            "event":"scan",
            "result":"bull"
        }
    )

    assert memory.size() == 1

    result = memory.recent()

    assert result[0]["event"] == "scan"