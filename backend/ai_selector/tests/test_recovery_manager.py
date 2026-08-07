from core.runtime.recovery_manager import RecoveryManager


def test_recovery_success():

    manager = RecoveryManager()

    result = manager.execute(
        lambda: "ok"
    )

    assert result == "ok"



def test_recovery_fallback():

    manager = RecoveryManager(
        max_retry=3
    )

    result = manager.execute(
        lambda: 1 / 0,
        fallback="cache"
    )

    assert result == "cache"



def test_retry_setting():

    manager = RecoveryManager(
        max_retry=5
    )

    assert manager.retry_count() == 5