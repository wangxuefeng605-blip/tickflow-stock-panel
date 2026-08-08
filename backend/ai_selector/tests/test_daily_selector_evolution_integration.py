from core.daily_ai_selector import run_daily_selector


def test_daily_selector_evolution_integration():

    result = run_daily_selector()

    assert result is True