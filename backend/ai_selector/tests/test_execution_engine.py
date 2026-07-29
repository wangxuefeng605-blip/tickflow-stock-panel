from core.execution.executor import Executor



def test_execution_buy():


    decision = {

        "code":"000001",

        "decision":"BUY",

        "confidence":0.9

    }


    order = Executor().execute(
        decision
    )


    assert order.action=="BUY"

    assert order.quantity==100