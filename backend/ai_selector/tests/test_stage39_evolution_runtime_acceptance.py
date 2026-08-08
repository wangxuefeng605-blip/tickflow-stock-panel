from core.evolution.evolution_runtime import EvolutionRuntime


def test_stage39_full_evolution_runtime():

    runtime = EvolutionRuntime()

    result = runtime.run(
        {
            "momentum":0.35,
            "trend":0.30
        }
    )

    assert result is not None

    assert "generation" in result

    assert result["generation"] == 1

    assert "strategy" in result