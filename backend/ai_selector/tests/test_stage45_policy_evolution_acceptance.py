from core.policy.policy_state import PolicyState
from core.policy.policy_registry import PolicyRegistry
from core.policy.policy_evaluator import PolicyEvaluator
from core.policy.policy_selector import PolicySelector


def test_stage45_policy_evolution():

    registry = PolicyRegistry()

    evaluator = PolicyEvaluator()

    policies = [
        PolicyState(version="v1"),
        PolicyState(version="v2")
    ]


    evaluator.evaluate(
        policies[0],
        {"score":0.6}
    )

    evaluator.evaluate(
        policies[1],
        {"score":0.95}
    )


    for policy in policies:
        registry.register(policy)


    selector = PolicySelector()

    best = selector.select(
        registry.list()
    )


    assert best.version == "v2"
    assert best.score == 0.95