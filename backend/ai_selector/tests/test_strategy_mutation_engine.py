from core.evolution.strategy_mutation_engine import (
    StrategyMutationEngine
)



def test_strategy_mutation():

    engine = StrategyMutationEngine()


    strategy = {
        "name":"momentum",
        "version":1,
        "score":80
    }


    result = engine.mutate(
        strategy
    )


    assert result["version"] == 2
    assert result["mutation"]



def test_generate_candidates():

    engine = StrategyMutationEngine()


    result = engine.generate_candidates(
        {
            "version":1,
            "score":50
        },
        5
    )


    assert len(result) == 5