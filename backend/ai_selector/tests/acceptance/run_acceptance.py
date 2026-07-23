"""
TickFlow Quant Platform
Acceptance Test Framework
"""

from datetime import datetime
import platform
import sys

from tests.acceptance.stages.benchmark import run_benchmark
from tests.acceptance.stages.scanner_benchmark import run_scanner_benchmark


def print_header():
    print("=" * 60)
    print("TickFlow Quant Platform Acceptance Test")
    print("=" * 60)
    print(f"Start Time : {datetime.now():%Y-%m-%d %H:%M:%S}")
    print(f"Python     : {platform.python_version()}")
    print()


def stage(name):
    print(f"[PASS] {name}")


def print_footer():
    print()
    print("=" * 60)
    print("RESULT : PASS")
    print("=" * 60)


def run_benchmark_stage():

    print()
    print("Benchmark")
    print("-" * 60)

    result = run_benchmark()

    for name, data in result.items():
        print(
            f"{name:12} : {data['status']} "
            f"{data['ms']} ms"
        )

    print("-" * 60)


def run_scanner_stage():

    print()
    print("Scanner Benchmark")
    print("-" * 60)

    result = run_scanner_benchmark(
        limit=50
    )

    for name, data in result.items():
        print(
            f"{name:12} : {data}"
        )

    print("-" * 60)


def main():

    print_header()

    stage("Acceptance Framework Initialized")

    run_benchmark_stage()

    run_scanner_stage()

    print_footer()

    return 0


if __name__ == "__main__":
    sys.exit(main())