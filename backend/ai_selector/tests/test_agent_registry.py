from core.agent_runtime.agent_registry import AgentRegistry


def test_agent_registry():

    registry = AgentRegistry()


    registry.register(
        "market",
        object()
    )


    assert registry.get("market") is not None