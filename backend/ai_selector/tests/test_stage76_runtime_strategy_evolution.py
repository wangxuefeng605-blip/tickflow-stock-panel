from core.runtime_strategy_evolution import RuntimeStrategyEvolution


def test_runtime_strategy_evolution():

    engine = RuntimeStrategyEvolution()


    result = engine.evolve(
        {
            "weight_adjustment": True
        }
    )


    assert result["strategy_updated"] is True

    assert result["version"] == 1