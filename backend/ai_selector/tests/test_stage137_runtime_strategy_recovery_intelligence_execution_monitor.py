from core.runtime_strategy_recovery_intelligence_execution_monitor import (
    RuntimeStrategyRecoveryIntelligenceExecutionMonitor
)



def test_execution_monitor_success():

    monitor = (
        RuntimeStrategyRecoveryIntelligenceExecutionMonitor()
    )


    result = monitor.monitor(
        {
            "success": True
        }
    )


    assert result["runtime_status"] == "healthy"
    assert result["health"] is True
    assert result["progress"] == 1.0



def test_execution_monitor_failure():

    monitor = (
        RuntimeStrategyRecoveryIntelligenceExecutionMonitor()
    )


    result = monitor.monitor(
        {
            "success": False,
            "error": "execution_failed"
        }
    )


    assert result["runtime_status"] == "failed"
    assert result["health"] is False
    assert "execution_failed" in result["alerts"]



def test_execution_monitor_history():

    monitor = (
        RuntimeStrategyRecoveryIntelligenceExecutionMonitor()
    )


    monitor.monitor(
        {
            "success": True
        }
    )


    assert len(
        monitor.get_history()
    ) == 1