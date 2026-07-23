"""
AI Scanner Report Writer
v17.3.1

Output:
    data/reports/top10.json
    data/reports/top10.csv
    data/reports/scan.log

Features:
    - Top10 JSON
    - Top10 CSV
    - Scan statistics
    - Human readable log
"""


import os
import json
import csv
from datetime import datetime


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



def save_json(
        top10,
        stats=None
):

    data = {

        "version": "v17.3.1",

        "market": "A-share",

        "update_time":
            datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "scan":
            stats or {},

        "count":
            len(top10),

        "data":
            top10
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
            indent=4
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
                "score"
            ]
        )


        writer.writeheader()

        writer.writerows(top10)



def save_log(
        top10,
        stats=None
):

    now = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    lines=[]


    lines.append(
        "="*40
    )

    lines.append(
        "AI Scanner v17.3.1"
    )

    lines.append(
        "="*40
    )


    lines.append(
        f"Time: {now}"
    )


    if stats:

        lines.append("")

        lines.append(
            "Scan Statistics"
        )

        lines.append(
            "-"*40
        )

        for k,v in stats.items():

            lines.append(
                f"{k}: {v}"
            )


    lines.append("")

    lines.append(
        "TOP10"
    )

    lines.append(
        "-"*40
    )


    for item in top10:

        lines.append(
            f"{item['rank']:>2}. "
            f"{item['code']} "
            f"score={item['score']:.4f}"
        )


    lines.append(
        "="*40
    )


    with open(
        LOG_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(
            "\n".join(lines)
        )



def write_report(
        top10,
        stats=None
):

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


    print(
        "Report generated:"
    )

    print(
        JSON_FILE
    )

    print(
        CSV_FILE
    )

    print(
        LOG_FILE
    )