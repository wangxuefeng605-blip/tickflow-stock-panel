from core.runtime_strategy_selection_engine import RuntimeStrategySelectionEngine


def test_runtime_strategy_selection_engine():

    engine = RuntimeStrategySelectionEngine()

    result = engine.select(
        [
            {
                "name":"A",
                "score":0.5
            },
            {
                "name":"B",
                "score":0.9
            }
        ]
    )

    assert result["name"] == "B"