from core.agent.agent_reasoner import AgentReasoner


def test_agent_reasoner():

    reasoner = AgentReasoner()


    result = reasoner.reason(
        {
            "score":0.8
        }
    )


    assert result["decision"] == "BUY"

    assert result["confidence"] == 0.8