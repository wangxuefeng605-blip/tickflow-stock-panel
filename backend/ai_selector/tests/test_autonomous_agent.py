from core.agent.autonomous_agent import AutonomousAgent


def test_autonomous_agent():

    agent = AutonomousAgent()


    result = agent.act(
        {
            "score":0.9
        }
    )


    assert result["decision"] == "BUY"

    assert agent.memory.size() == 1