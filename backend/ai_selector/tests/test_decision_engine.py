from core.intelligence.decision_engine import AIDecisionEngine


class Context:

    market_state="BEAR"



def test_ai_decision():

    engine=AIDecisionEngine()


    result=engine.decide(

        {
            "code":"603580",
            "score":0.8,
            "confidence":0.9
        },

        Context()

    )


    assert result.action=="BUY"