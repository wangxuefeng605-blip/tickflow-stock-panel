import csv
from pathlib import Path
from datetime import datetime


FAILED_FILE = Path(
    "data/cache/failed_stock.csv"
)


def save_failed_stock(
        code,
        reason,
        days
):

    FAILED_FILE.parent.mkdir(
        parents=True,
        exist_ok=True
    )


    exists = FAILED_FILE.exists()


    with open(
        FAILED_FILE,
        "a",
        newline="",
        encoding="utf-8"
    ) as f:

        writer = csv.writer(f)


        if not exists:
            writer.writerow(
                [
                    "date",
                    "code",
                    "reason",
                    "days"
                ]
            )


        writer.writerow(
            [
                datetime.now().date(),
                code,
                reason,
                days
            ]
        )