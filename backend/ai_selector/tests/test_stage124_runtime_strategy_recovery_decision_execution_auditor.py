from core.runtime_strategy_recovery_decision_execution_auditor import (
    RuntimeStrategyRecoveryDecisionExecutionAuditor
)


def test_runtime_strategy_execution_audit():

    auditor = (
        RuntimeStrategyRecoveryDecisionExecutionAuditor()
    )


    result = auditor.audit(
        {
            "policy": "restore",
            "action": "AUTO_EXECUTE",
            "risk": 0.2
        }
    )


    assert result["status"] == "AUDITED"



def test_runtime_strategy_block_audit():

    auditor = (
        RuntimeStrategyRecoveryDecisionExecutionAuditor()
    )


    result = auditor.audit(
        {
            "policy": "rollback",
            "action": "BLOCK",
            "risk": 0.9
        }
    )


    assert result["action"] == "BLOCK"



def test_runtime_strategy_audit_history():

    auditor = (
        RuntimeStrategyRecoveryDecisionExecutionAuditor()
    )


    auditor.audit(
        {
            "policy": "fallback",
            "action": "REVIEW_REQUIRED",
            "risk": 0.5
        }
    )


    assert len(
        auditor.get_history()
    ) == 1