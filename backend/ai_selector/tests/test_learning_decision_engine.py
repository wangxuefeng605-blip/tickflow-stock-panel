from core.learning.decision_engine import LearningDecisionEngine


def test_accept_learning():

    engine = LearningDecisionEngine()

    result = engine.decide(
        {
            "win_rate":0.6,
            "average_return":0.02
        }
    )

    assert result["decision"] == "accept"



def test_hold_learning():

    engine = LearningDecisionEngine()

    result = engine.decide(
        {
            "win_rate":0.4,
            "average_return":-0.01
        }
    )

    assert result["decision"] == "hold"