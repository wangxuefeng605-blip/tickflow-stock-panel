from core.runtime_metrics import RuntimeMetrics



def test_runtime_observability():

    metrics = RuntimeMetrics()


    metrics.record_success()

    metrics.record_failure()

    metrics.record_retry()

    metrics.record_recovery()


    result = metrics.report()


    assert result["total_runs"] == 2

    assert result["success_runs"] == 1

    assert result["failed_runs"] == 1

    assert result["retry_count"] == 1

    assert result["recovery_success"] == 1