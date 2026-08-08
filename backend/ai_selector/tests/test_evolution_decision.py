from core.evolution.evolution_decision import EvolutionDecision


def test_decision_replace():

    engine = EvolutionDecision()


    result = engine.decide(
        {
            "reward":0.5
        },
        [
            {
                "reward":0.8
            },
            {
                "reward":0.6
            }
        ]
    )


    assert result["decision"]=="REPLACE"



def test_decision_keep():

    engine = EvolutionDecision()


    result = engine.decide(
        {
            "reward":0.9
        },
        [
            {
                "reward":0.8
            }
        ]
    )


    assert result["decision"]=="KEEP"