from core.optimization.strategy_benchmark import StrategyBenchmark


def test_strategy_benchmark():

    benchmark = StrategyBenchmark()


    benchmark.record(
        "strategy_v1",
        0.85
    )


    results = benchmark.get_results()


    assert len(results) == 1

    assert results[0]["strategy"] == "strategy_v1"

    assert results[0]["performance"] == 0.85