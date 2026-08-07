from core.evolution.evolution_memory import EvolutionMemory



def test_save_strategy():

    memory = EvolutionMemory()

    result = memory.save_strategy(
        {
            "id":1,
            "name":"momentum_v1",
            "score":80
        }
    )


    assert result



def test_best_strategy():

    memory = EvolutionMemory()


    memory.save_strategy(
        {
            "id":1,
            "score":60
        }
    )


    memory.save_strategy(
        {
            "id":2,
            "score":90
        }
    )


    best = memory.best_strategy()


    assert best["id"] == 2