from core.runtime.runtime_logger import RuntimeLogger


def test_runtime_logger_write():

    logger = RuntimeLogger()

    logger.log(
        "scanner",
        "OK",
        duration=1.23
    )

    logs = logger.read_logs()

    assert len(logs) >= 1

    last = logs[-1]

    assert last["component"] == "scanner"
    assert last["status"] == "OK"



def test_runtime_logger_error():

    logger = RuntimeLogger()

    logger.log(
        "learning",
        "ERROR",
        error=ValueError("failed")
    )

    logs = logger.read_logs()

    last = logs[-1]

    assert last["status"] == "ERROR"
    assert "failed" in last["error"]