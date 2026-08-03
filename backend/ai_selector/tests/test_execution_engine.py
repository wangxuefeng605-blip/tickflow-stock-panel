from core.execution import ExecutionEngine
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

def test_execution_engine():

    engine = ExecutionEngine()

    decision = {
        "code": "000001",
        "action": "BUY",
        "confidence": 0.85
    }

    plan = engine.create_plan(
        decision
    )

    assert plan.code == "000001"
    assert plan.side == "BUY"
    assert plan.status == "CREATED"