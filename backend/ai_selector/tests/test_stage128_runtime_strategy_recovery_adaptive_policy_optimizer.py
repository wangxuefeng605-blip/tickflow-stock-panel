from core.runtime_strategy_recovery_adaptive_policy_optimizer import (
    RuntimeStrategyRecoveryAdaptivePolicyOptimizer
)


def test_runtime_strategy_best_policy():

    optimizer = (
        RuntimeStrategyRecoveryAdaptivePolicyOptimizer()
    )


    optimizer.update_weights(
        {
            "restore": 1.2,
            "rollback": 0.9,
            "fallback": 1.0
        }
    )


    result = optimizer.optimize()


    assert result["selected_policy"] == "restore"



def test_runtime_strategy_policy_weight():

    optimizer = (
        RuntimeStrategyRecoveryAdaptivePolicyOptimizer()
    )


    optimizer.update_weights(
        {
            "restore": 1.3
        }
    )


    result = optimizer.optimize()


    assert result["weight"] == 1.3



def test_runtime_strategy_optimizer_history():

    optimizer = (
        RuntimeStrategyRecoveryAdaptivePolicyOptimizer()
    )


    optimizer.optimize()


    assert len(
        optimizer.get_history()
    ) == 1