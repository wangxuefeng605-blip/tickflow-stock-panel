from core.runtime_strategy_alert_manager import (
    RuntimeStrategyAlertManager
)



def test_runtime_strategy_warning_alert():

    manager = RuntimeStrategyAlertManager()


    alert = manager.create_alert(
        {
            "type": "reward_drift",
            "drop": 0.4
        }
    )


    assert (
        alert["level"]
        ==
        "warning"
    )



def test_runtime_strategy_critical_alert():

    manager = RuntimeStrategyAlertManager()


    alert = manager.create_alert(
        {
            "type": "execution_failure_spike",
            "failure_rate": 0.9
        }
    )


    assert (
        alert["level"]
        ==
        "critical"
    )



def test_runtime_strategy_alert_history():

    manager = RuntimeStrategyAlertManager()


    manager.create_alert(
        {
            "type": "behavior_deviation"
        }
    )


    assert len(
        manager.history()
    ) == 1