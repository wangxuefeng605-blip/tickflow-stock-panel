from core.runtime_strategy_recovery_adaptive_strategy_evolution_engine import (
    RuntimeStrategyRecoveryAdaptiveStrategyEvolutionEngine
)


def test_runtime_strategy_evolution_strengthen():

    engine = (
        RuntimeStrategyRecoveryAdaptiveStrategyEvolutionEngine()
    )


    result = engine.evolve(
        {
            "strategy": "restore",
            "optimization_action": "increase",
            "weight_adjustment": 0.1
        }
    )


    assert result["evolution"] == "strengthen"
    assert result["weight"] == 1.1



def test_runtime_strategy_evolution_weaken():

    engine = (
        RuntimeStrategyRecoveryAdaptiveStrategyEvolutionEngine()
    )


    result = engine.evolve(
        {
            "strategy": "fallback",
            "optimization_action": "decrease",
            "weight_adjustment": -0.1
        }
    )


    assert result["evolution"] == "weaken"



def test_runtime_strategy_evolution_history():

    engine = (
        RuntimeStrategyRecoveryAdaptiveStrategyEvolutionEngine()
    )


    engine.evolve(
        {
            "strategy": "restore",
            "optimization_action": "increase",
            "weight_adjustment": 0.1
        }
    )


    assert len(
        engine.get_history()
    ) == 1