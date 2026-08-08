from core.evolution.evolution_state import EvolutionState



def test_evolution_state():


    state = EvolutionState()


    state.add_strategy(
        {
            "name":"momentum_v2"
        }
    )


    state.evolve_generation()


    state.set_best(
        {
            "name":"momentum_v2"
        }
    )


    result = state.snapshot()


    assert result["generation"] == 1

    assert result["strategy_count"] == 1

    assert (
        result["best_strategy"]["name"]
        ==
        "momentum_v2"
    )