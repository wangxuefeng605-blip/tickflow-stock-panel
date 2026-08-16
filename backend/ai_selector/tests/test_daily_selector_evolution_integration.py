from unittest.mock import patch, MagicMock

from core.daily_ai_selector import run_daily_selector


def test_daily_selector_evolution_integration():

    fake_top10 = [
        {
            "code": "000001",
            "score": 0.8
        }
    ]


    with patch(
        "core.daily_ai_selector.run_fast_scan",
        return_value=fake_top10
    ), patch(
        "core.daily_ai_selector.load_top10_result",
        return_value=fake_top10
    ), patch(
        "core.daily_ai_selector.save_daily_recommendation"
    ), patch(
        "core.daily_ai_selector.generate_report",
        return_value={}
    ), patch(
        "core.daily_ai_selector.run_tracker"
    ), patch(
        "core.daily_ai_selector.generate_summary"
    ), patch(
        "core.daily_ai_selector.FeedbackLearningService"
    ) as mock_feedback, patch(
        "core.daily_ai_selector.DailyEvolutionHook"
    ) as mock_evolution, patch(
        "core.daily_ai_selector.LearningRuntimeService"
    ) as mock_learning:


        mock_feedback.return_value.learn.return_value = {
            "momentum":0.3
        }


        mock_evolution.return_value.evolve.return_value = {
            "status":"EVOLVED"
        }


        mock_learning.return_value.record_prediction.return_value = []


        mock_learning.return_value.process_daily.return_value = None


        result = run_daily_selector()


    assert result is True