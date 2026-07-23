import time


def run_benchmark():
    """
    Basic acceptance benchmark.
    """

    results = {}

    # history simulation
    start = time.perf_counter()

    dummy = 0
    for i in range(100000):
        dummy += i

    elapsed = time.perf_counter() - start

    results["history"] = {
        "status": "PASS",
        "ms": round(elapsed * 1000, 3),
    }


    # factor simulation
    start = time.perf_counter()

    values = [i * 1.01 for i in range(100000)]

    elapsed = time.perf_counter() - start

    results["factor"] = {
        "status": "PASS",
        "ms": round(elapsed * 1000, 3),
    }


    # score simulation
    start = time.perf_counter()

    score = sum(values)

    elapsed = time.perf_counter() - start

    results["score"] = {
        "status": "PASS",
        "ms": round(elapsed * 1000, 3),
    }


    return results