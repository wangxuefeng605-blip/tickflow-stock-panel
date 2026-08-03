import json

from pathlib import Path
from datetime import datetime


BASE_DIR = Path(
    "data/learning/outcomes"
)

BASE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


class OutcomeTracker:


    def __init__(self):

        self.base_dir = BASE_DIR



    def save_prediction_outcome(
        self,
        code,
        prediction_date,
        score,
        result=None
    ):


        record = {

            "timestamp":
                datetime.now().isoformat(),

            "code":
                str(code),

            "prediction_date":
                prediction_date,

            "score":
                score,

            "result":
                result or {}

        }


        filename = (

            str(code)

            +

            "_"

            +

            datetime.now()
            .strftime("%Y%m%d_%H%M%S")

            +

            ".json"

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



    def load_all(
        self
    ):


        records = []


        files = sorted(
            self.base_dir.glob("*.json")
        )


        for file in files:

            with open(
                file,
                encoding="utf-8"
            ) as f:

                records.append(
                    json.load(f)
                )


        return records



    def update_result(
        self,
        code,
        result
    ):


        files = sorted(
            self.base_dir.glob(
                f"{code}_*.json"
            ),
            reverse=True
        )


        if not files:
            return None


        file = files[0]


        with open(
            file,
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        data["result"] = result


        with open(
            file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2
            )


        return file