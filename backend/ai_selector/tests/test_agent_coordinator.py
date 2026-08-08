from core.agent_runtime.agent_coordinator import AgentCoordinator


def test_agent_coordinator():

    coordinator = AgentCoordinator()

    result = coordinator.coordinate(
        {
            "market":"BULL"
        }
    )

    assert result is not None