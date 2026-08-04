from core.runtime_strategy_recovery_dynamic_policy_rebalancer import (
    RuntimeStrategyRecoveryDynamicPolicyRebalancer
)


def test_runtime_strategy_policy_rebalance():

    rebalancer = (
        RuntimeStrategyRecoveryDynamicPolicyRebalancer()
    )

    result = rebalancer.rebalance(
        {
            "fallback": 1.1,
            "rollback": 0.9,
            "restore": 1.2
        }
    )

    assert round(
        sum(result.values()),
        5
    ) == 1.0



def test_runtime_strategy_policy_normalization():

    rebalancer = (
        RuntimeStrategyRecoveryDynamicPolicyRebalancer()
    )

    result = rebalancer.rebalance(
        {
            "fallback": 2,
            "rollback": 2
        }
    )

    assert result["fallback"] == 0.5



def test_runtime_strategy_policy_rebalance_history():

    rebalancer = (
        RuntimeStrategyRecoveryDynamicPolicyRebalancer()
    )

    rebalancer.rebalance(
        {
            "fallback": 1
        }
    )

    assert len(
        rebalancer.get_history()
    ) == 1