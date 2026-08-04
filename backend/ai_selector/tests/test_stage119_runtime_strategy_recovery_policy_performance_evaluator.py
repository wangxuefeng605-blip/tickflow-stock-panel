from core.runtime_strategy_recovery_policy_performance_evaluator import (
    RuntimeStrategyRecoveryPolicyPerformanceEvaluator
)


def test_runtime_strategy_policy_performance():

    evaluator = (
        RuntimeStrategyRecoveryPolicyPerformanceEvaluator()
    )

    result = evaluator.evaluate(
        "fallback",
        success=8,
        failure=2,
        avg_recovery_time=1
    )

    assert result["policy"] == "fallback"
    assert result["success_rate"] == 0.8



def test_runtime_strategy_policy_score():

    evaluator = (
        RuntimeStrategyRecoveryPolicyPerformanceEvaluator()
    )

    result = evaluator.evaluate(
        "restore",
        success=10,
        failure=0,
        avg_recovery_time=0
    )

    assert result["score"] >= 1



def test_runtime_strategy_policy_performance_history():

    evaluator = (
        RuntimeStrategyRecoveryPolicyPerformanceEvaluator()
    )

    evaluator.evaluate(
        "rollback",
        success=5,
        failure=1
    )

    assert len(
        evaluator.get_history()
    ) == 1