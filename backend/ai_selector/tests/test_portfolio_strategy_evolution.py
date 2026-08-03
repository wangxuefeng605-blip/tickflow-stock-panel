from core.portfolio.strategy_evolver import StrategyEvolver


evolver = StrategyEvolver()


def test_bull_strategy():

    result = evolver.evolve(
        "BULL",
        {
            "reward": 0.8
        }
    )

    assert result["momentum"] > 0