from core.runtime_health_monitor import RuntimeHealthMonitor


def test_runtime_health_monitor():

    monitor = RuntimeHealthMonitor()


    result = monitor.check(
        {
            "runtime_healthy": True
        }
    )


    assert result["health_checked"] is True

    assert result["runtime_healthy"] is True

    assert result["status"] == "READY"