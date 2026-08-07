from core.healing.recovery_strategy import (
    AdaptiveRecoveryStrategy
)



def test_adaptive_strategy():

    strategy = AdaptiveRecoveryStrategy()


    result = strategy.decide(
        {
            "type":"TIMEOUT",
            "action":"RETRY"
        }
    )


    assert result["retry"] == 3



def test_strategy_learning():

    strategy = AdaptiveRecoveryStrategy()


    for _ in range(5):

        strategy.record_result(
            "TIMEOUT",
            False
        )


    result = strategy.decide(
        {
            "type":"TIMEOUT"
        }
    )


    assert result["retry"] == 5