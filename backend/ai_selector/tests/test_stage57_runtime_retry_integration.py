from core.retry_manager import RetryManager


def test_runtime_retry_integration():

    retry = RetryManager()

    result = retry.add_failed(
        "000001",
        "worker failed"
    )

    assert "000001" in result