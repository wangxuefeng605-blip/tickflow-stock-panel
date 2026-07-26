from pathlib import Path
import csv
from datetime import datetime


FILE = Path(
    "data/cache/failed_stock.csv"
)


def record_failed_stock(code, reason):

    FILE.parent.mkdir(
        exist_ok=True
    )

    exists = FILE.exists()

    with open(
        FILE,
        "a",
        newline="",
        encoding="utf8"
    ) as f:

        writer = csv.writer(f)

        if not exists:
            writer.writerow(
                [
                    "code",
                    "reason",
                    "time"
                ]
            )

        writer.writerow(
            [
                code,
                reason,
                datetime.now()
            ]
        )