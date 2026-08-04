from core.runtime_strategy_recovery_policy_selector import (
    RuntimeStrategyRecoveryPolicySelector
)



def test_runtime_strategy_recovery_policy_selector_best():

    selector = RuntimeStrategyRecoveryPolicySelector()


    result = selector.select(
        {
            "fallback": 1.2,
            "rollback": 0.8,
            "parameter_restore": 1.0
        }
    )


    assert result["selected_policy"] == "fallback"
    assert result["confidence"] == 1.2



def test_runtime_strategy_recovery_policy_selector_second_case():

    selector = RuntimeStrategyRecoveryPolicySelector()


    result = selector.select(
        {
            "fallback": 0.5,
            "rollback": 1.5,
            "parameter_restore": 1.0
        }
    )


    assert result["selected_policy"] == "rollback"



def test_runtime_strategy_recovery_policy_selector_history():

    selector = RuntimeStrategyRecoveryPolicySelector()


    selector.select(
        {
            "fallback": 1.1,
            "rollback": 1.0
        }
    )


    assert len(
        selector.selection_history()
    ) == 1