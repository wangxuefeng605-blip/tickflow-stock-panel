from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_fitness_optimizer import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveFitnessOptimizer
)



def test_fitness_optimization():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveFitnessOptimizer()
    )


    result = optimizer.optimize(
        {
            "strategy": "adaptive_restore",
            "reward": 1.0,
            "previous_fitness": 0
        }
    )


    assert result["fitness"] == 0.7
    assert result["optimized"] is True



def test_fitness_with_history():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveFitnessOptimizer()
    )


    result = optimizer.optimize(
        {
            "strategy": "restore",
            "reward": 0.8,
            "previous_fitness": 0.5
        }
    )


    assert result["fitness"] == 0.71



def test_candidate_compare():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveFitnessOptimizer()
    )


    result = optimizer.compare(
        [
            {
                "strategy": "a",
                "fitness": 0.5
            },
            {
                "strategy": "b",
                "fitness": 0.9
            }
        ]
    )


    assert result["strategy"] == "b"



def test_fitness_history():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveFitnessOptimizer()
    )


    optimizer.optimize(
        {
            "strategy": "test",
            "reward": 1
        }
    )


    assert len(
        optimizer.get_history()
    ) == 1