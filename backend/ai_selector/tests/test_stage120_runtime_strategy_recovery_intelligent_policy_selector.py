from core.runtime_strategy_recovery_intelligent_policy_selector import (
    RuntimeStrategyRecoveryIntelligentPolicySelector
)


def test_runtime_strategy_intelligent_policy_selection():

    selector = (
        RuntimeStrategyRecoveryIntelligentPolicySelector()
    )


    result = selector.select(
        {
            "fallback": {
                "weight": 0.3,
                "score": 0.7
            },
            "restore": {
                "weight": 0.8,
                "score": 0.9
            }
        }
    )


    assert result["selected_policy"] == "restore"



def test_runtime_strategy_policy_score():

    selector = (
        RuntimeStrategyRecoveryIntelligentPolicySelector()
    )


    result = selector.select(
        {
            "rollback": {
                "weight": 1,
                "score": 0.5
            }
        }
    )


    assert result["score"] == 0.5



def test_runtime_strategy_selection_history():

    selector = (
        RuntimeStrategyRecoveryIntelligentPolicySelector()
    )


    selector.select(
        {
            "fallback": {
                "weight": 1,
                "score": 1
            }
        }
    )


    assert len(
        selector.get_history()
    ) == 1