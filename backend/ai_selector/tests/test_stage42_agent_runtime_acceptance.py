from core.agent_runtime.agent_runtime import AgentRuntime


def test_stage42_agent_runtime():

    runtime = AgentRuntime()

    result = runtime.run(
        {
            "market": "bull",
            "stocks": [
                "000001",
                "000002"
            ]
        }
    )

    assert result is not None