from core.evolution.mutation_engine import MutationEngine


def test_mutation_engine():

    engine = MutationEngine()


    result = engine.mutate(
        {
            "momentum":0.5,
            "trend":0.3
        }
    )


    assert "strategy" in result

    assert "mutation" in result

    assert result["mutation"]["type"] == "parameter"