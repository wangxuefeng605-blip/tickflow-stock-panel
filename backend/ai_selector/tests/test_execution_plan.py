from core.execution.execution_plan import ExecutionPlan


def test_execution_plan():

    plan = ExecutionPlan(
        code="000001",
        action="BUY",
        confidence=0.8
    )

    assert plan.code == "000001"