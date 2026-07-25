import os
import csv
from datetime import datetime

FAILED_FILE = "data/cache/failed_stock.csv"


class RetryManager:
    def __init__(self):
        self.current_failed = []

        os.makedirs(os.path.dirname(FAILED_FILE), exist_ok=True)

        if not os.path.exists(FAILED_FILE):
            with open(FAILED_FILE, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(
                    ["code", "error", "retry_count", "last_time"]
                )

    def add_failed(self, code, error, retry_count=1):
        code = str(code)

        if code not in self.current_failed:
            self.current_failed.append(code)

        rows = []

        if os.path.exists(FAILED_FILE):
            with open(FAILED_FILE, "r", encoding="utf-8") as f:
                rows = list(csv.DictReader(f))

        found = False

        for row in rows:
            if row["code"] == code:
                row["error"] = str(error)
                row["retry_count"] = str(int(row["retry_count"]) + 1)
                row["last_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                found = True
                break

        if not found:
            rows.append(
                {
                    "code": code,
                    "error": str(error),
                    "retry_count": str(retry_count),
                    "last_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
            )

        with open(FAILED_FILE, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=["code", "error", "retry_count", "last_time"],
            )
            writer.writeheader()
            writer.writerows(rows)

    def get_failed_codes(self):
        if not os.path.exists(FAILED_FILE):
            return []

        with open(FAILED_FILE, "r", encoding="utf-8") as f:
            return [row["code"] for row in csv.DictReader(f)]

    def get_current_failed_codes(self):
        return list(self.current_failed)