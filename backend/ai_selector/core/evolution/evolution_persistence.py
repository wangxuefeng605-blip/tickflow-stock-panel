"""
Evolution Persistence

Stage54.2
"""

import json
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(
    "data/evolution"
)

STRATEGY_FILE = (
    BASE_DIR /
    "current_strategy.json"
)

HISTORY_FILE = (
    BASE_DIR /
    "evolution_history.json"
)


class EvolutionPersistence:


    def __init__(self):

        BASE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )


    def save_strategy(
        self,
        strategy
    ):

        with open(
            STRATEGY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                strategy,
                f,
                indent=2,
                ensure_ascii=False
            )


        return True



    def load_strategy(
        self
    ):

        if not STRATEGY_FILE.exists():

            return None


        with open(
            STRATEGY_FILE,
            encoding="utf-8"
        ) as f:

            return json.load(f)



    def append_history(
        self,
        result
    ):

        history = []


        if HISTORY_FILE.exists():

            with open(
                HISTORY_FILE,
                encoding="utf-8"
            ) as f:

                history = json.load(f)


        result = {
            **result,
            "timestamp":
                datetime.now().isoformat()
        }


        history.append(
            result
        )


        with open(
            HISTORY_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                history,
                f,
                indent=2,
                ensure_ascii=False
            )


        return result