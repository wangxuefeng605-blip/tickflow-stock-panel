from core.daily_scheduler import start_scheduler


def test_scheduler_import():

    assert callable(
        start_scheduler
    )