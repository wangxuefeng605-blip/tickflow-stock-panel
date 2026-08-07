from core.optimization.strategy_evolution_engine import (
    StrategyEvolutionEngine
)



def test_strategy_evolution():


    engine = StrategyEvolutionEngine()


    result = engine.evaluate(
        {
            "ranking": 1,
            "learning": -1,
        }
    )


    assert (
        result["ranking"]
        ==
        1.1
    )


    assert (
        result["learning"]
        ==
        0.9
    )


    assert (
        engine.best_strategy()
        ==
        "ranking"
    )