import json
from pathlib import Path


class RuntimeStrategyStateStorage:
    """
    Runtime strategy state persistence layer.
    """

    def __init__(self, path="data/runtime_strategy_state.json"):
        self.path = Path(path)

    def save(self, state):

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as f:
            json.dump(
                state,
                f,
                indent=2
            )

        return {
            "saved": True,
            "state": state
        }


    def load(self):

        if not self.path.exists():

            return {
                "loaded": False,
                "state": {}
            }


        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            state = json.load(f)


        return {
            "loaded": True,
            "state": state
        }