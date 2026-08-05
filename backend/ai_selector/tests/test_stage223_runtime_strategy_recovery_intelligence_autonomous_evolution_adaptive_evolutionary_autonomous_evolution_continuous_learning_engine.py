from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evolutionary_autonomous_evolution_continuous_learning_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContinuousLearningEngine
)



def test_add_experience():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContinuousLearningEngine()
    )


    result = engine.add_experience(
        {
            "profit": 100
        }
    )


    assert result["stored"] is True



def test_learning():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContinuousLearningEngine()
    )


    engine.add_experience(
        {
            "profit": 100
        }
    )


    engine.add_experience(
        {
            "profit": -20
        }
    )


    result = engine.learn()


    assert result["success_rate"] == 0.5



def test_parameter_update():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContinuousLearningEngine()
    )


    engine.add_experience(
        {
            "profit": 50
        }
    )


    engine.learn()


    result = engine.get_parameters()


    assert result["confidence"] == 1



def test_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvolutionaryAutonomousEvolutionContinuousLearningEngine()
    )


    engine.add_experience(
        {
            "profit": 1
        }
    )


    assert len(
        engine.get_history()
    ) == 1