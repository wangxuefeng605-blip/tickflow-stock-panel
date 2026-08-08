from core.agent.autonomous_agent import AutonomousAgent


def test_stage41_autonomous_agent():

    agent = AutonomousAgent()


    result = agent.act(
        {
            "momentum":0.8,
            "trend":0.7
        }
    )


    assert result is not None

    assert "decision" in result

    assert agent.memory.size() == 1