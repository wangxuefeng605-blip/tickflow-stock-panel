import json

from pathlib import Path


BASE_DIR = Path(
    "data/learning/decisions"
)


BASE_DIR.mkdir(
    parents=True,
    exist_ok=True
)


class DecisionStore:


    def __init__(self):

        self.base_dir = BASE_DIR



    def save(
        self,
        record
    ):

        path = (
            self.base_dir
            /
            f"{record.code}.json"
        )


        with open(
            path,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                record.to_dict(),
                f,
                ensure_ascii=False,
                indent=2
            )


        return path



    def load_all(self):

        records = []


        for file in self.base_dir.glob(
            "*.json"
        ):

            with open(
                file,
                encoding="utf-8"
            ) as f:

                records.append(
                    json.load(f)
                )


        return records