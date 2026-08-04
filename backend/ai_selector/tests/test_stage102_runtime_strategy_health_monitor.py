from core.runtime_strategy_health_monitor import (
    RuntimeStrategyHealthMonitor
)



def test_runtime_strategy_health_monitor():

    monitor = RuntimeStrategyHealthMonitor()


    result = monitor.evaluate(
        {
            "execution_success_rate": 0.95,
            "reward_score": 0.85,
            "stability": 0.9
        }
    )


    assert (
        result["status"]
        ==
        "healthy"
    )


    assert (
        result["health_score"]
        >
        0.8
    )



def test_runtime_strategy_health_degraded():

    monitor = RuntimeStrategyHealthMonitor()


    result = monitor.evaluate(
        {
            "execution_success_rate": 0.2,
            "reward_score": 0.3,
            "stability": 0.2
        }
    )


    assert (
        result["status"]
        ==
        "degraded"
    )