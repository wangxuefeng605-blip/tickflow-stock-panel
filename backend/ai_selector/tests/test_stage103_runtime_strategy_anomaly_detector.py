from core.runtime_strategy_anomaly_detector import (
    RuntimeStrategyAnomalyDetector
)



def test_runtime_strategy_anomaly_reward():

    detector = RuntimeStrategyAnomalyDetector()


    result = detector.detect_reward_drift(
        [
            0.9,
            0.8,
            0.5
        ]
    )


    assert result["anomaly"] is True

    assert (
        result["type"]
        ==
        "reward_drift"
    )



def test_runtime_strategy_execution_failure():

    detector = RuntimeStrategyAnomalyDetector()


    result = detector.detect_execution_failure(
        [
            True,
            False,
            False,
            False
        ]
    )


    assert result["anomaly"] is True



def test_runtime_strategy_behavior():

    detector = RuntimeStrategyAnomalyDetector()


    result = detector.detect_behavior_deviation(
        "long_hold",
        "short_hold"
    )


    assert result["anomaly"] is True