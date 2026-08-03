from core.execution.execution_plan import ExecutionPlan
from core.execution.execution_state import ExecutionTracker


def test_execution_state_flow():

    plan = ExecutionPlan(
        code="000001",
        side="BUY"
    )

    tracker = ExecutionTracker()

    tracker.update(plan)

    assert len(tracker.history) == 1