from core.runtime.decision_policy import (
    RuntimeDecisionPolicy
)


def test_policy_continue():

    policy = RuntimeDecisionPolicy()

    result = policy.apply(
        {
            "action": "CONTINUE"
        }
    )

    assert result["mode"] == "NORMAL"



def test_policy_recovery():

    policy = RuntimeDecisionPolicy(
        max_retry=5
    )

    result = policy.apply(
        {
            "action": "RECOVER_SCANNER"
        }
    )

    assert result["mode"] == "RECOVERY"
    assert result["retry"] == 5
    assert result["target"] == "scanner"



def test_policy_safe():

    policy = RuntimeDecisionPolicy()

    result = policy.apply(
        {
            "action": "SAFE_MODE"
        }
    )

    assert result["mode"] == "SAFE"