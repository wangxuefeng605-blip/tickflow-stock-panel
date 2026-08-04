from core.retry_manager import RetryManager
from core.retry_executor import RetryExecutor


def test_retry_execution_loop():

    retry = RetryManager()

    retry.add_failed(
        "000001",
        "worker failed"
    )


    executor = RetryExecutor()

    result = executor.run_retry()


    assert result["retry_completed"] is True

    assert "000001" in result["failed_tasks"]