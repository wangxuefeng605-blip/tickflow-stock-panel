from core.runtime.runtime_health import RuntimeHealth


def test_runtime_health_ok():

    health = RuntimeHealth()

    health.update(
        "scanner",
        "OK"
    )

    health.update(
        "ranking",
        "OK"
    )

    health.update(
        "learning",
        "OK"
    )

    health.update(
        "cache",
        "OK"
    )

    health.mark_run_complete()

    result = health.report()

    assert result["status"] == "HEALTHY"
    assert result["last_run"] is not None


def test_runtime_health_error():

    health = RuntimeHealth()

    health.record_error(
        "scanner",
        "timeout"
    )

    result = health.report()

    assert result["status"] == "DEGRADED"
    assert len(result["errors"]) == 1