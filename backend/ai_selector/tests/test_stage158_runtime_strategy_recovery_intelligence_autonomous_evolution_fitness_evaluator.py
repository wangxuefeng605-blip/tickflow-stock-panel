from core.runtime_strategy_recovery_intelligence_autonomous_evolution_fitness_evaluator import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionFitnessEvaluator
)



def test_fitness_calculation():

    evaluator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionFitnessEvaluator()
    )


    result = evaluator.evaluate(
        {
            "strategy": "restore",
            "optimized_reward": 1.0,
            "stability": 1.0
        }
    )


    assert result["fitness"] == 1.0



def test_fitness_with_risk():

    evaluator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionFitnessEvaluator()
    )


    result = evaluator.evaluate(
        {
            "strategy": "rollback",
            "optimized_reward": 0.5,
            "stability": 0.5
        }
    )


    assert result["fitness"] == 0.5



def test_fitness_history():

    evaluator = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionFitnessEvaluator()
    )


    evaluator.evaluate(
        {
            "strategy": "test",
            "optimized_reward": 0.8
        }
    )


    assert len(
        evaluator.get_history()
    ) == 1