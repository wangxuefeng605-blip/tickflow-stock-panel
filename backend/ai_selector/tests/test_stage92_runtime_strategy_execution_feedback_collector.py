from core.runtime_strategy_execution_feedback_collector import (
    RuntimeStrategyExecutionFeedbackCollector
)


def test_runtime_strategy_execution_feedback_collector():

    collector = RuntimeStrategyExecutionFeedbackCollector()


    result = collector.collect(
        {
            "strategy":"momentum",
            "success":True
        }
    )


    assert result["collected"] is True
    assert result["execution"]["success"] is True