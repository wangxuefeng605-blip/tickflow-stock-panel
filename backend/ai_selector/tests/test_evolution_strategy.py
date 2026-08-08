from core.evolution.evolution_strategy import EvolutionStrategy


def test_strategy_mutation():

    engine = EvolutionStrategy()


    result = engine.mutate(
        {
            "momentum":0.35,
            "trend":0.30,
            "quality":0.15,
            "liquidity":0.10,
            "risk":0.10
        }
    )


    assert len(result) == 3


    for strategy in result:

        assert round(
            sum(strategy.values()),
            4
        ) == 1