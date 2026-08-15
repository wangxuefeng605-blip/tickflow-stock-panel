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
from core.runtime.runtime_guard import RuntimeGuard
from core.runtime.runtime_guard import RuntimeGuard
from core.evolution.daily_evolution_hook import (
    DailyEvolutionHook
)
from core.evolution.evolution_weight_provider import (
    EvolutionWeightProvider
)
from core.feedback.learning_service import (
    FeedbackLearningService
)
from core.fast_scanner import run_fast_scan


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


    return [
        x for x in data
        if isinstance(x, dict)
    ]

def print_header():

    print("=" * 60)

    print(" AI Selector Daily Runner ")

    print("=" * 60)

    print(
        "Run Date:",
        datetime.now()
    )

class DailyAISelector:

    def __init__(self):

        self.guard = RuntimeGuard()


    def run(self):

        return run_daily_selector()


    def health(self):

        return self.guard.report()

def run_daily_selector():

    start = time.time()
    print(
        "Loading Evolution Weights..."
    )


    weight_provider = (
        EvolutionWeightProvider()
    )


    evolution_weights = (
        weight_provider.get_weights()
    )


    print(
        "Evolution Weights:",
        evolution_weights
    )

    print(
        "Applying Feedback Learning..."
    )


    feedback_service = (
        FeedbackLearningService()
    )


    learned_weights = (
        feedback_service.learn(
            evolution_weights
        )
    )


    print(
        "Feedback Learned Weights:",
        learned_weights
    )
    
    guard = RuntimeGuard()

    print_header()


    print()

    print("Starting Scanner...")


    run_fast_scan(
        weights=learned_weights
    )

    print(
        "Saving AI Recommendation History..."
    )


    top10 = load_top10_result()


    save_daily_recommendation(
        top10
    )


    print(
        "Running Evolution Hook..."
    )
    top_score = 0

    if top10:
        first = top10[0]

        if isinstance(first, dict):
            top_score = first.get(
               "score",
                0
            )

    evolution_hook = DailyEvolutionHook()

    evolution_result = evolution_hook.evolve(
    {
        "strategy": "daily_top10",
        "score": top_score
    }
)


    print(
        "Evolution Result:",
        evolution_result
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
def build_evolution_input(top10):

    if not top10:
        return {
            "strategy":"empty",
            "score":0
        }


    avg_score = sum(
        item.get(
            "score",
            0
        )
        for item in top10
    ) / len(top10)


    return {
        "strategy":"daily_top10",
        "score":avg_score
    }
   

if __name__ == "__main__":

    run_daily_selector()
