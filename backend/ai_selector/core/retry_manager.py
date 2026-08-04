import os
import csv
from datetime import datetime

FAILED_FILE = "data/cache/failed_stock.csv"

class RetryManager:
    def __init__(self):
        os.makedirs(os.path.dirname(FAILED_FILE), exist_ok=True)

        if not os.path.exists(FAILED_FILE):
            with open(FAILED_FILE, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["code", "error", "retry_count", "last_time"])

    def add_failed(self, code, error, retry_count=1):

        rows = []

        if os.path.exists(FAILED_FILE):
            with open(
                FAILED_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                reader = csv.DictReader(f)

                for row in reader:
                    if None in row:
                        row.pop(None)

                    rows.append(row)


        found = False

        for row in rows:

            if row["code"] == str(code):

                row["error"] = str(error)
                row["retry_count"] = str(
                    int(row["retry_count"]) + 1
                )
                row["last_time"] = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )

                found = True
                break


        if not found:

            rows.append(
                {
                    "code": str(code),
                    "error": str(error),
                    "retry_count": str(retry_count),
                    "last_time": datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )
                }
            )


        with open(
            FAILED_FILE,
            "w",
            encoding="utf-8",
            newline=""
        ) as f:

            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "code",
                    "error",
                    "retry_count",
                    "last_time"
                ],
                extrasaction="ignore"
            )

            writer.writeheader()
            writer.writerows(rows)


        return [
            row["code"]
            for row in rows
        ]
            

    def get_failed(self):

        if not os.path.exists(FAILED_FILE):
            return []

        with open(
            FAILED_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            reader = csv.DictReader(f)

            result = []

            for row in reader:

                if row.get("code"):
                    result.append(row["code"])

            return result