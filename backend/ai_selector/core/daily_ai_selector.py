"""
Daily AI Selector Runner
"""

import time
import runpy

from datetime import datetime
from core.report_generator import generate_report
from core.recommendation_history import (
    save_daily_recommendation
)


def print_header():

    print("=" * 60)

    print(" AI Selector Daily Runner ")

    print("=" * 60)

    print(
        "Run Date:",
        datetime.now()
    )



def run_daily_selector():

    start = time.time()


    print_header()


    print()

    print("Starting Scanner...")


    runpy.run_module(
        "core.fast_scanner",
        run_name="__main__"
    )

    print("Generating AI TOP10 Report...")

    reports = generate_report()

    print(reports)

    elapsed = time.time() - start


    print()

    print("=" * 60)

    print("Daily AI Selector Finished")

    print(
        "Elapsed:",
        round(elapsed,2),
        "seconds"
    )

    print("=" * 60)



    return True



if __name__ == "__main__":

    run_daily_selector()