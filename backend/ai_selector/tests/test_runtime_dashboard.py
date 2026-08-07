from core.observability.runtime_dashboard import (
    RuntimeDashboard
)


def test_dashboard_health():

    dashboard = RuntimeDashboard(
        snapshot={
            "scanner": "OK"
        },

        metrics={
            "scanner_latency": 1,
            "error_count": 0,
        },

        analyzer=type(
            "Analyzer",
            (),
            {
                "analyze":
                lambda s, m:
                {
                    "performance": "GOOD"
                }
            }
        )(),

        alerts=[]
    )


    result = dashboard.generate()


    assert (
        result["runtime"]
        == "HEALTHY"
    )


def test_dashboard_degraded():

    dashboard = RuntimeDashboard(
        {},
        {},
        type(
            "Analyzer",
            (),
            {
                "analyze":
                lambda s, m:
                {}
            }
        )(),

        [
            {
                "error": "failure"
            }
        ]
    )


    result = dashboard.generate()


    assert (
        result["runtime"]
        == "DEGRADED"
    )