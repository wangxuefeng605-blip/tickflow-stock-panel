from core.decision import DecisionStrategyBridge



def test_decision_strategy_bridge():


    bridge = DecisionStrategyBridge()


    decision = {

        "code":"000001",

        "action":"BUY",

        "confidence":0.8

    }


    result = bridge.apply(
        decision
    )


    assert "strategy" in result