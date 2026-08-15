from pathlib import Path
import json


class FeedbackStorage:

    def __init__(self):
        self.path = (
            Path("data")
            / "feedback"
            / "records.json"
        )

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True
        )


    def save(self, record):

        records = self.load()

        records.append(record)

        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                records,
                f,
                ensure_ascii=False,
                indent=2
            )


    def load(self):

        if not self.path.exists():
            return []

        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as f:

            return json.load(f)