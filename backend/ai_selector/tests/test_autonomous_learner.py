from core.learning.autonomous_learner import AutonomousLearner


def test_autonomous_learner():

    learner = AutonomousLearner()

    result = learner.learn(
        {
            "strategy": "trend",
            "score": 0.91,
            "return": 0.08
        }
    )

    assert result["strategy"] == "trend"
    assert result["reward"] == 0.08