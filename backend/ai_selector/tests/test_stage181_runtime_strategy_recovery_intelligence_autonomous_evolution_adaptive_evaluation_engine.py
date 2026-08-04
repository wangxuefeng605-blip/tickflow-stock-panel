from core.runtime_strategy_recovery_intelligence_autonomous_evolution_adaptive_evaluation_engine import (
    RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvaluationEngine
)



def test_improvement_accept():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvaluationEngine()
    )


    result = engine.evaluate(
        {
            "fitness": 0.5
        },
        {
            "fitness": 0.8
        }
    )


    assert result["decision"] == "accept"
    assert result["improvement"] == 0.3



def test_same_fitness_continue():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvaluationEngine()
    )


    result = engine.evaluate(
        {
            "fitness": 0.5
        },
        {
            "fitness": 0.5
        }
    )


    assert result["decision"] == "continue"



def test_regression_rollback():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvaluationEngine()
    )


    result = engine.evaluate(
        {
            "fitness": 0.8
        },
        {
            "fitness": 0.3
        }
    )


    assert result["decision"] == "rollback"



def test_evaluation_history():

    engine = (
        RuntimeStrategyRecoveryIntelligenceAutonomousEvolutionAdaptiveEvaluationEngine()
    )


    engine.evaluate(
        {
            "fitness": 1
        },
        {
            "fitness": 1
        }
    )


    assert len(
        engine.get_history()
    ) == 1