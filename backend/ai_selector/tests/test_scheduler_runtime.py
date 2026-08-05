from core.runtime_lock import (
    acquire_lock,
    release_lock
)


def test_runtime_lock():

    release_lock()

    assert acquire_lock()

    assert not acquire_lock()

    release_lock()