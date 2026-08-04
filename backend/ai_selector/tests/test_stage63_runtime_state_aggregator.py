from core.runtime_state import RuntimeStateAggregator



def test_runtime_state_aggregator():

    aggregator = RuntimeStateAggregator()


    result = aggregator.build(

        health={
            "runtime_healthy": True,
            "status": "READY"
        },

        metrics={
            "total_runs": 100,
            "success_runs": 98,
            "retry_count": 5
        },

        healing={
            "self_healing_completed": True
        }

    )


    assert result["runtime_status"] == "READY"

    assert result["health"] == "READY"

    assert result["success_rate"] == 0.98

    assert result["retry_count"] == 5

    assert result["self_healing"] is True