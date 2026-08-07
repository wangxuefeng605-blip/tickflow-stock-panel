from core.runtime.runtime_guard import RuntimeGuard


def test_runtime_guard_success():

    guard = RuntimeGuard()

    result = guard.run(
        "scanner",
        lambda: "success"
    )

    assert result == "success"

    report = guard.report()

    assert (
        report["components"]["scanner"]
        == "OK"
    )


def test_runtime_guard_failure():

    guard = RuntimeGuard()

    result = guard.run(
        "scanner",
        lambda: 1 / 0,
        fallback="fallback"
    )

    assert result == "fallback"

    report = guard.report()

    assert (
        report["components"]["scanner"]
        == "ERROR"
    )