"""
AI Scanner Report Writer
v17.4
"""

import os
import json
import csv
from datetime import datetime
from dataclasses import asdict, is_dataclass


class JSONEncoder(json.JSONEncoder):

    def default(self, obj):

        if is_dataclass(obj):
            return asdict(obj)

        if hasattr(obj, "__dict__"):
            return obj.__dict__

        return super().default(obj)



def normalize_results(results):

    output = []

    for item in results:

        if is_dataclass(item):
            output.append(
                asdict(item)
            )

        elif hasattr(item, "__dict__"):
            output.append(
                item.__dict__
            )

        else:
            output.append(item)

    return output



BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


REPORT_DIR = os.path.join(
    BASE_DIR,
    "data",
    "reports"
)

os.makedirs(
    REPORT_DIR,
    exist_ok=True
)


JSON_FILE = os.path.join(
    REPORT_DIR,
    "top10.json"
)

CSV_FILE = os.path.join(
    REPORT_DIR,
    "top10.csv"
)

LOG_FILE = os.path.join(
    REPORT_DIR,
    "scan.log"
)



def save_json(top10, stats=None):

    data = {

        "version": "v17.4",

        "market": "A-share",

        "update_time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "scan": stats or {},

        "count": len(top10),

        "data": top10
    }


    with open(
        JSON_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4,
            cls=JSONEncoder
        )



def save_csv(top10):

    with open(
        CSV_FILE,
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=[
                "rank",
                "code",
                "score",
                "confidence",
                "signals"
            ],
            extrasaction="ignore"
        )


        writer.writeheader()

        writer.writerows(top10)



def save_log(top10, stats=None):

    lines = []

    lines.append("=" * 40)
    lines.append("AI Scanner v17.4")
    lines.append("=" * 40)

    lines.append(
        datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )
    )


    lines.append("")
    lines.append("TOP10")
    lines.append("-" * 40)


    for item in top10:

        lines.append(
            f"{item.get('rank',0):>2}. "
            f"{item.get('code')} "
            f"score={item.get('score',0):.4f}"
        )


    with open(
        LOG_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "\n".join(lines)
        )



def write_report(top10, stats=None):

    top10 = normalize_results(top10)


    save_json(
        top10,
        stats
    )


    save_csv(
        top10
    )


    save_log(
        top10,
        stats
    )


    print("Report generated:")
    print(JSON_FILE)
    print(CSV_FILE)
    print(LOG_FILE)