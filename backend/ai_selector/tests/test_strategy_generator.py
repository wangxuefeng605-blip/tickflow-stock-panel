from core.evolution.strategy_generator import StrategyGenerator


def test_strategy_generator():

    generator = StrategyGenerator()


    result = generator.generate(
        {
            "momentum":0.5,
            "trend":0.3
        }
    )


    assert len(result) == 2

    assert result[0]["momentum"] == 0.5

    assert "trend" in result[1]