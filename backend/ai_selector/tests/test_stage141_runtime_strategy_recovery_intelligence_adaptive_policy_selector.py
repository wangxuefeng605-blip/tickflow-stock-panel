from core.runtime_strategy_recovery_intelligence_adaptive_policy_selector import (
    RuntimeStrategyRecoveryIntelligenceAdaptivePolicySelector
)



def test_policy_selector_best_policy():

    selector = (
        RuntimeStrategyRecoveryIntelligenceAdaptivePolicySelector()
    )


    selector.register_policy(
        {
            "policy_version": 1,
            "policy_score": 0.5
        }
    )


    selector.register_policy(
        {
            "policy_version": 2,
            "policy_score": 0.8
        }
    )


    result = selector.select()


    assert result["policy"] == 2
    assert result["score"] == 0.8



def test_policy_selector_empty():

    selector = (
        RuntimeStrategyRecoveryIntelligenceAdaptivePolicySelector()
    )


    result = selector.select()


    assert result["policy"] is None
    assert result["score"] == 0



def test_policy_selector_history():

    selector = (
        RuntimeStrategyRecoveryIntelligenceAdaptivePolicySelector()
    )


    selector.select()


    assert len(
        selector.get_history()
    ) == 1