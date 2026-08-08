from core.agent_runtime.agent_runtime import AgentRuntime


def test_agent_runtime():

    runtime = AgentRuntime()

    runtime.register(
        "test",
        object()
    )

    result = runtime.run()

    assert result is not None