from core.runtime_strategy_recovery_intelligence_autonomous_evolution_reward_optimizer import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionRewardOptimizer
)



def test_reward_success_bonus():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionRewardOptimizer()
    )


    result = optimizer.optimize(
        {
            "strategy": "restore",
            "reward": 1.0,
            "success": True
        }
    )


    assert result["optimized_reward"] == 1.1



def test_reward_failure_penalty():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionRewardOptimizer()
    )


    result = optimizer.optimize(
        {
            "strategy": "rollback",
            "reward": 0.0,
            "success": False
        }
    )


    assert result["optimized_reward"] == -0.1



def test_reward_history():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionRewardOptimizer()
    )


    optimizer.optimize(
        {
            "strategy": "test",
            "reward": 0.5,
            "success": True
        }
    )


    assert len(
        optimizer.get_history()
    ) == 1