from core.agent.agent_controller import AgentController


def test_agent_controller():

    controller = AgentController()


    result = controller.run(
        {
            "score":0.9
        }
    )


    assert result["decision"] == "BUY"

    assert len(controller.history) == 1