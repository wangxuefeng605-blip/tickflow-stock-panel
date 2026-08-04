import time

from core.scanner.runtime_integration import ScannerRuntimeIntegration


def test_runtime_performance_validation():

    runtime = ScannerRuntimeIntegration()


    start = time.perf_counter()


    count = 100

    for _ in range(count):

        result = runtime.run(
            {
                "code": "000001",
                "momentum": 0.8
            }
        )


        assert result["runtime_ready"]

        assert result["worker_execution_completed"]


    elapsed = time.perf_counter() - start


    avg = elapsed / count


    print(
        f"\nRuntime Performance:"
        f"\nCalls: {count}"
        f"\nTotal: {elapsed:.6f}s"
        f"\nAverage: {avg*1000:.3f}ms"
    )


    # 当前 runtime 只是 orchestration 层，
    # 允许较宽松阈值
    assert avg < 0.05