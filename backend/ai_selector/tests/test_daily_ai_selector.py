from core.daily_ai_selector import run_daily_selector


def test_daily_runner_import():

    assert callable(
        run_daily_selector
    )