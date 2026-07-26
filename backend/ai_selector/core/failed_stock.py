import csv
from datetime import datetime
from pathlib import Path


FAILED_FILE = Path(
    "data/cache/failed_stock.csv"
)


def record_failed(
    code,
    stage,
    reason,
    days=0,
    retry_count=0
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
            writer.writerow([
                "code",
                "stage",
                "reason",
                "days",
                "retry_count",
                "last_time"
            ])


        writer.writerow([
            code,
            stage,
            reason,
            days,
            retry_count,
            datetime.now()
        ])