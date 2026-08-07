from core.evolution.evolution_controller import EvolutionController


def test_evolution_controller():

    controller = EvolutionController()

    result = controller.evolve(
        {
            "momentum":0.35,
            "trend":0.30
        }
    )

    assert result is not None
    assert "strategy" in result