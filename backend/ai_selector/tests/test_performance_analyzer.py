from core.observability.performance_analyzer import (
    PerformanceAnalyzer
)


def test_performance_good():

    analyzer = PerformanceAnalyzer()

    result = analyzer.analyze(
        {
            "scanner_latency": 1,
            "error_count": 0,
        }
    )

    assert (
        result["performance"]
        == "GOOD"
    )


def test_performance_warning():

    analyzer = PerformanceAnalyzer()

    result = analyzer.analyze(
        {
            "scanner_latency": 10,
            "error_count": 1,
        }
    )

    assert (
        "runtime_error"
        in result["issues"]
    )