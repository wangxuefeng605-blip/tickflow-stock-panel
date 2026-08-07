from core.observability.alert_manager import (
    AlertManager
)


def test_alert_trigger():

    manager = AlertManager()

    alert = manager.check(
        "error_count",
        5,
        3
    )

    assert alert is not None

    assert (
        alert["metric"]
        == "error_count"
    )


def test_no_alert():

    manager = AlertManager()

    alert = manager.check(
        "error_count",
        1,
        3
    )

    assert alert is None