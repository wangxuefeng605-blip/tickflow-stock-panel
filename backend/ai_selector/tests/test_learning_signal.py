from core.learning.learning_signal import (
    LearningSignalGenerator
)


def test_generate_signal():

    generator = LearningSignalGenerator()


    performance = {
        "success_rate": 0.7,
        "avg_return": 0.08
    }


    result = generator.generate(
        performance
    )


    assert "signals" in result
    assert result["confidence"] == 0.7
    assert result["signals"]["momentum"] > 0