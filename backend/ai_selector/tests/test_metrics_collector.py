from core.observability.metrics_collector import (
    MetricsCollector
)


def test_metrics_record():

    collector = MetricsCollector()

    collector.record(
        "scanner_latency",
        0.52
    )

    data = collector.snapshot()

    assert (
        data["metrics"]["scanner_latency"]
        == 0.52
    )


def test_metrics_increment():

    collector = MetricsCollector()

    collector.increment(
        "error_count"
    )

    data = collector.snapshot()

    assert (
        data["metrics"]["error_count"]
        == 1
    )