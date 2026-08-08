from core.evolution.daily_evolution_hook import (
    DailyEvolutionHook
)


def test_daily_evolution_hook():

    hook = DailyEvolutionHook()

    result = hook.evolve(
        {
            "strategy": "trend",
            "score": 0.91
        }
    )

    assert result["strategy"] == "trend"

    assert "mutation" in result