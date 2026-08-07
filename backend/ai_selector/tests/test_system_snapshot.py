from core.observability.system_snapshot import (
    SystemSnapshot
)


def test_snapshot_update():

    snapshot = SystemSnapshot()

    snapshot.update(
        "runtime",
        {
            "status": "OK"
        }
    )

    result = snapshot.generate()

    assert (
        result["components"]["runtime"]["status"]
        == "OK"
    )


def test_snapshot_created_time():

    snapshot = SystemSnapshot()

    result = snapshot.generate()

    assert (
        result["created_at"]
        is not None
    )