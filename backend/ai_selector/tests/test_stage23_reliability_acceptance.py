from core.runtime.runtime_health import RuntimeHealth
from core.runtime.runtime_guard import RuntimeGuard
from core.runtime.recovery_manager import RecoveryManager
from core.runtime.runtime_logger import RuntimeLogger


def test_stage23_reliability_full_chain():

    health = RuntimeHealth()

    # 根据 runtime_health.py 实际接口修改这里
    result = health.report()

    assert result is not None


    guard = RuntimeGuard()

    output = guard.run(
        "scanner",
        lambda: "OK"
    )

    assert output == "OK"


    recovery = RecoveryManager()

    recovered = recovery.execute(
        lambda: "SUCCESS"
    )

    assert recovered == "SUCCESS"


    logger = RuntimeLogger()

    logger.log(
        "stage23",
        "OK"
    )

    logs = logger.read_logs()

    assert len(logs) > 0