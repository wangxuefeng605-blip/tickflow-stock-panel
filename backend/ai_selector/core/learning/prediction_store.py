import json
from pathlib import Path
from datetime import datetime


BASE_DIR = Path(
    "data/learning"
)

FILE = BASE_DIR / "predictions.json"


class PredictionStore:


    def __init__(self):

        BASE_DIR.mkdir(
            parents=True,
            exist_ok=True
        )


    def save(
        self,
        results
    ):

        records = []


        if FILE.exists():

            records = json.loads(
                FILE.read_text(
                    encoding="utf-8"
                )
            )


        for item in results:

            records.append({

                "code": item.code,

                "score": item.score,

                "market_state":
                    item.market_state,

                "confidence":
                    item.confidence,

                "scan_date":
                    datetime.now().isoformat()

            })


        FILE.write_text(
            json.dumps(
                records,
                indent=2,
                ensure_ascii=False
            ),
            encoding="utf-8"
        )