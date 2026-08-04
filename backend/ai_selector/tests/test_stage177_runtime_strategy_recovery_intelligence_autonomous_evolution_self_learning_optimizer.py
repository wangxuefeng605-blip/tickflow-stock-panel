from core.runtime_strategy_recovery_intelligence_autonomous_evolution_self_learning_optimizer import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionSelfLearningOptimizer
)



def test_high_fitness_learning():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionSelfLearningOptimizer()
    )


    result = optimizer.learn(
        {
            "fitness": 0.9
        }
    )


    assert result["config"]["mutation_rate"] == 0.05
    assert result["config"]["crossover_rate"] == 0.7



def test_low_fitness_learning():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionSelfLearningOptimizer()
    )


    result = optimizer.learn(
        {
            "fitness": 0.3
        }
    )


    assert result["config"]["mutation_rate"] == 0.2



def test_config_access():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionSelfLearningOptimizer()
    )


    config = optimizer.get_config()


    assert config["population_size"] == 5



def test_learning_history():

    optimizer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionSelfLearningOptimizer()
    )


    optimizer.learn(
        {
            "fitness": 1
        }
    )


    assert len(
        optimizer.get_history()
    ) == 1