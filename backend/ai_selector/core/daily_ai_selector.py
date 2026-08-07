"""
Daily AI Selector Runner
"""

import time
import runpy
import json

from pathlib import Path
from datetime import datetime
from core.report_generator import generate_report
from core.recommendation_history import (
    save_daily_recommendation
)
from core.performance_tracker import run_tracker
from core.performance_summary import generate_summary
from core.learning_engine import run_learning
from core.learning.daily_feedback_runner import (
    DailyFeedbackRunner
)
from core.learning.runtime_service import (
    LearningRuntimeService
)
from core.learning import LearningRuntimeService

def load_top10_result():

    path = Path(
        "data/reports/top10.json"
    )


    if not path.exists():

        print(
            "TOP10 file not found"
        )

        return []


    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)


    if isinstance(data, dict):

        return data.get(
            "data",
            []
        )


    return data

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

    print(
        "Saving AI Recommendation History..."
    )


    top10 = load_top10_result()

    save_daily_recommendation(
        top10
    )

    print(
        "Recording Learning Prediction..."
    )


    learning_service = LearningRuntimeService()


    prediction_paths = (
        learning_service
        .record_prediction(
            top10,
            datetime.now().strftime(
                "%Y-%m-%d"
            )
        )
    )


    print(
        "Prediction records:",
        prediction_paths
    )


    print(
        "Saved recommendations:",
        len(top10)
    )

    print("Generating AI TOP10 Report...")

    reports = generate_report()

    print(reports)

    


    print("Generating Performance Report...")


    run_tracker()


    print("Generating Performance Summary...")


    generate_summary()


    print("Running AI Learning Engine...")


    learning_service = (
        LearningRuntimeService()
    )


    learning_service.process_daily(
      top10,
        datetime.now().strftime(
            "%Y-%m-%d"
        )
    )

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


def apply_learning_weights(weights):

    runner = DailyFeedbackRunner()

    feedbacks = []

    return runner.update(
        weights,
        feedbacks
    )

   

if __name__ == "__main__":

    run_daily_selector()