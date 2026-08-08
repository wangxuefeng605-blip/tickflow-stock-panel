from core.agent.agent_state import AgentState


def test_agent_state():

    state = AgentState()

    assert state.status == "IDLE"


    state.activate()

    assert state.status == "ACTIVE"


    state.record(
        {
            "event":"market_scan"
        }
    )


    result = state.snapshot()


    assert result["memory_size"] == 1