from core.runtime_strategy_recovery_intelligence_autonomous_learning_optimizer import (
    RuntimeStrategyRecoveryIntelligenceAutonomousLearningOptimizer
)



def test_learning_optimizer_reward():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousLearningOptimizer()
    )


    result = optimizer.optimize(
        {
            "score_delta": 0.1
        }
    )


    assert result["policy_weight"] == 1.1
    assert result["strategy_score"] == 0.6
    assert result["optimized"] is True



def test_learning_optimizer_penalty():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousLearningOptimizer()
    )


    result = optimizer.optimize(
        {
            "score_delta": -0.1
        }
    )


    assert result["policy_weight"] == 0.9
    assert result["strategy_score"] == 0.4



def test_learning_optimizer_history():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousLearningOptimizer()
    )


    optimizer.optimize(
        {
            "score_delta": 0.1
        }
    )


    assert len(
        optimizer.get_history()
    ) == 1