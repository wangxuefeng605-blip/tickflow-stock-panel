from core.evolution.evolution_loop import EvolutionLoop


def test_evolution_loop():

    loop = EvolutionLoop()

    result = loop.run(
        {
            "strategy": "trend",
            "score": 0.91
        }
    )

    assert result["strategy"] == "trend"
    assert result["mutation"] == "increase_weight"