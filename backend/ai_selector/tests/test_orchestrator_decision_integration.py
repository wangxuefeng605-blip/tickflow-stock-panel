from core.orchestrator.adapters.decision_adapter import DecisionAdapter
from core.intelligence.decision_engine import AIDecisionEngine



def test_decision_adapter():


    adapter = DecisionAdapter(
        AIDecisionEngine()
    )


    item = type(
        "RankingResult",
        (),
        {

            "code":"000001",

            "score":0.8,

            "confidence":0.9,

            "market_state":"BULL"

        }
    )


    result = adapter.run(
        [
            item()
        ]
    )


    assert result[0].code=="000001"