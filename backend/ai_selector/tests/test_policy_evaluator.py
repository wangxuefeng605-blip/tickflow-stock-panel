from core.policy.policy_state import PolicyState
from core.policy.policy_evaluator import PolicyEvaluator


def test_policy_evaluator():

    policy = PolicyState(
        version="v1"
    )

    evaluator = PolicyEvaluator()

    result = evaluator.evaluate(
        policy,
        {
            "score":0.9
        }
    )

    assert result["version"] == "v1"
    assert result["score"] == 0.9
    assert policy.score == 0.9