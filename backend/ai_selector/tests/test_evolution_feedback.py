from core.evolution.evolution_feedback import EvolutionFeedback


def test_evolution_feedback():

    feedback = EvolutionFeedback()


    result = feedback.evaluate(
        {
            "return":0.12
        }
    )


    assert result["reward"] == 1
    assert result["success"] is True