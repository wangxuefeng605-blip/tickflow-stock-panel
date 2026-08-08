from core.evolution.evolution_persistence import (
    EvolutionPersistence
)


def test_evolution_persistence():


    store = EvolutionPersistence()


    strategy = {
        "momentum":0.4,
        "trend":0.3,
        "reward":0.85
    }


    assert (
        store.save_strategy(
            strategy
        )
        is True
    )


    loaded = (
        store.load_strategy()
    )


    assert (
        loaded["reward"]
        ==
        0.85
    )



def test_evolution_history():


    store = EvolutionPersistence()


    result = (
        store.append_history(
            {
                "decision":"REPLACE",
                "reward":0.9
            }
        )
    )


    assert (
        result["decision"]
        ==
        "REPLACE"
    )