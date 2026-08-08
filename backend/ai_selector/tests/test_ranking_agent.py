from core.agent_runtime.ranking_agent import RankingAgent


def test_ranking_agent():

    agent = RankingAgent()

    result = agent.run(
        {
            "candidates": [
                {"code":"000001","score":90}
            ]
        }
    )

    assert result["leader"]["code"] == "000001"