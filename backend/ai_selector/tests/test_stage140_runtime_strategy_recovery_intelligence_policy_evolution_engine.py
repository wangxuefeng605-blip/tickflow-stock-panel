from core.runtime_strategy_recovery_intelligence_policy_evolution_engine import (
    RuntimeStrategyRecoveryIntelligencePolicyEvolutionEngine
)



def test_policy_evolution_reward():

    engine = (
        RuntimeStrategyRecoveryIntelligencePolicyEvolutionEngine()
    )


    result = engine.evolve(
        {
            "learning_signal": "reward",
            "weight_delta": 0.1
        }
    )


    assert result["action"] == "increase"
    assert result["policy_version"] == 2



def test_policy_evolution_penalty():

    engine = (
        RuntimeStrategyRecoveryIntelligencePolicyEvolutionEngine()
    )


    result = engine.evolve(
        {
            "learning_signal": "penalty",
            "weight_delta": -0.1
        }
    )


    assert result["action"] == "decrease"
    assert result["policy_score"] == 0.4



def test_policy_evolution_history():

    engine = (
        RuntimeStrategyRecoveryIntelligencePolicyEvolutionEngine()
    )


    engine.evolve(
        {
            "learning_signal": "reward",
            "weight_delta": 0.1
        }
    )


    assert len(
        engine.get_history()
    ) == 1