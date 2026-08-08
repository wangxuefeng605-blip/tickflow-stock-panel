from core.evolution.evolution_reward import (
    EvolutionReward
)


def test_evolution_reward():

    reward = EvolutionReward()


    result = reward.calculate(
        [
            {
                "return":0.12
            },
            {
                "return":0.05
            },
            {
                "return":-0.03
            }
        ]
    )


    assert result["samples"] == 3

    assert result["success_rate"] > 0

    assert result["average_reward"] > 0