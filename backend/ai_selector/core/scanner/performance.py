import time
from collections import defaultdict


class PerformanceTracker:

    def __init__(self):

        self.metrics = defaultdict(
            lambda: {
                "count": 0,
                "total": 0.0
            }
        )


    def record(
        self,
        name,
        elapsed
    ):

        item = self.metrics[name]

        item["count"] += 1
        item["total"] += elapsed


    def report(self):

        print("\n")
        print("=" * 40)
        print(" Scanner Performance Report ")
        print("=" * 40)

        for name, item in self.metrics.items():

            avg = (
                item["total"]
                /
                item["count"]
                *
                1000
            )

            print(
                f"{name:<10}"
                f" count={item['count']:<6}"
                f" avg={avg:.3f}ms"
            )

        print("=" * 40)
        import json


def save(self, path):

    data = {}

    for name,item in self.metrics.items():

        data[name] = {
            "count": item["count"],
            "avg_ms":
                item["total"]
                /
                item["count"]
                *
                1000
        }


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )