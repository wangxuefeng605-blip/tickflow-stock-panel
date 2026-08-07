from core.optimization.performance_optimizer import (
    PerformanceOptimizer
)



def test_performance_optimizer():


    optimizer = PerformanceOptimizer()


    optimizer.record(
        "scanner",
        2
    )


    optimizer.record(
        "ranking",
        0.2
    )


    result = optimizer.analyze()


    assert (
        result["scanner"]
        ==
        "SLOW"
    )


    assert (
        result["ranking"]
        ==
        "NORMAL"
    )


    actions = optimizer.optimize()


    assert len(actions) == 1