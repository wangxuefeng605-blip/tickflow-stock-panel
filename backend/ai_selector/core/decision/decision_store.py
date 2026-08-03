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

        self.latest = None



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


        self.latest = path

        return path



    def load_all(self):

        records=[]


        files = list(
            self.base_dir.glob("*.json")
        )


        if self.latest and self.latest.exists():

            files.remove(self.latest)

            files.insert(
                0,
                self.latest
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