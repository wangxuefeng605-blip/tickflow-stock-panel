import json
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(
    "data/learning/predictions"
)

BASE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


class PredictionStore:


    def __init__(self):

        self.base_dir = BASE_DIR



    def save(
        self,
        predictions,
        market_state="UNKNOWN",
        weights=None
    ):

        record = {

            "timestamp":
                datetime.now().isoformat(),

            "market_state":
                market_state,

            "weights":
                weights or {},

            "stocks":
                predictions
        }


        filename = (
            datetime.now()
            .strftime("%Y%m%d_%H%M%S")
            + ".json"
        )


        path = (
            self.base_dir
            /
            filename
        )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                record,
                f,
                ensure_ascii=False,
                indent=2
            )


        return path



    def load_all(self):

        records = []


        for file in sorted(
            self.base_dir.glob("*.json")
        ):

            with open(
                file,
                encoding="utf-8"
            ) as f:

                records.append(
                    json.load(f)
                )


        return records