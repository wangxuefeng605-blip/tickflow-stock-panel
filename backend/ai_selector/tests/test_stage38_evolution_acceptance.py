from core.evolution.evolution_controller import EvolutionController


def test_stage38_full_evolution_loop():

    controller = EvolutionController()


    result = controller.evolve(
        {
            "momentum":0.5,
            "trend":0.3
        }
    )


    assert result["generation"] == 1

    assert "best_strategy" in result

    assert result["best_strategy"]["momentum"] > 0.5