from core.evolution.evolution_runtime import EvolutionRuntime


def test_evolution_runtime():

    runtime = EvolutionRuntime()


    result = runtime.run(
        {
            "momentum":0.35,
            "trend":0.30
        }
    )


    assert result["status"] == "EVOLVED"

    assert result["generation"] >= 1

    assert "strategy" in result