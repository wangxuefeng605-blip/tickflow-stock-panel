"""
Scanner Performance Monitor V3
"""

from __future__ import annotations

import time

from collections import defaultdict


class Performance:

    def __init__(self):

        self.reset()

    # -----------------------------

    def reset(self):

        self.stats = defaultdict(list)

    # -----------------------------

    class Timer:

        def __init__(self, owner, name):

            self.owner = owner
            self.name = name

        def __enter__(self):

            self.start = time.perf_counter()

        def __exit__(self, exc_type, exc, tb):

            cost = time.perf_counter() - self.start

            self.owner.stats[self.name].append(cost)

    # -----------------------------

    def timer(self, name):

        return self.Timer(self, name)

    # -----------------------------

    def report(self):

        print("=" * 40)
        print(" Scanner Performance Report ")
        print("=" * 40)

        if not self.stats:

            print("No performance data.")
            print("=" * 40)
            return

        for name, values in self.stats.items():

            total = sum(values)

            avg = total / len(values)

            print(
                f"{name:<10}"
                f" count={len(values):<5}"
                f" total={total:.4f}s"
                f" avg={avg*1000:.2f}ms"
            )

        print("=" * 40)


# 全局单实例
perf = Performance()

# 兼容旧代码
performance = perf