from core.daily_ai_selector import DailyAISelector


def test_observability_full_chain():

    selector = DailyAISelector()

    result = selector.run()

    assert result