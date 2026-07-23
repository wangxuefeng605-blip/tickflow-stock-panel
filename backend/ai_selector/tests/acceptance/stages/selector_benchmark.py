import time


def run_selector_benchmark():

    result = {}

    start = time.perf_counter()

    try:

        from ranking import run_ranking

        data = run_ranking()

        elapsed = time.perf_counter() - start


        result["selector"] = {
            "status": "PASS",
            "seconds": round(elapsed,3),
            "stocks": len(data)
        }


    except Exception as e:

        result["selector"] = {
            "status": "FAIL",
            "error":str(e)
        }


    return result