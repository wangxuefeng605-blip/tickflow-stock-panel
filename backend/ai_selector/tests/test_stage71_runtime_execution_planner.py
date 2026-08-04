from core.runtime_execution_planner import RuntimeExecutionPlanner


def test_runtime_execution_planner():

    planner = RuntimeExecutionPlanner()


    result = planner.plan()


    assert "tasks" in result

    assert "workers" in result