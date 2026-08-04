from core.runtime_strategy_recovery_intelligence_autonomous_evolution_neural_decision_layer import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionNeuralDecisionLayer
)



def test_high_fitness_exploit():

    layer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionNeuralDecisionLayer()
    )


    result = layer.decide(
        {
            "fitness": 0.9,
            "diversity": 0.2
        }
    )


    assert result["action"] == "exploit"



def test_high_diversity_explore():

    layer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionNeuralDecisionLayer()
    )


    result = layer.decide(
        {
            "fitness": 0.5,
            "diversity": 0.9
        }
    )


    assert result["action"] == "explore"



def test_low_fitness_rollback():

    layer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionNeuralDecisionLayer()
    )


    result = layer.decide(
        {
            "fitness": 0.1,
            "diversity": 0.2
        }
    )


    assert result["action"] == "rollback"



def test_decision_history():

    layer = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionNeuralDecisionLayer()
    )


    layer.decide(
        {
            "fitness": 0.5
        }
    )


    assert len(
        layer.get_history()
    ) == 1