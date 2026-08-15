import csv
import json
from pathlib import Path


REPORT_DIR = Path("data/reports")


def serialize_item(item):
    """Convert ranking result objects into JSON-serializable values."""

    if item is None:
        return None

    if isinstance(item, dict):
        return {
            key: serialize_item(value)
            for key, value in item.items()
        }

    if isinstance(item, (list, tuple)):
        return [
            serialize_item(value)
            for value in item
        ]

    if hasattr(item, "__dict__"):
        return serialize_item(vars(item))

    return item


def save_full_ranking(results):
    """Write complete ranking and TOP10 to JSON, plus full ranking CSV."""

    REPORT_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    json_path = REPORT_DIR / "full_ranking.json"
    csv_path = REPORT_DIR / "full_ranking.csv"
    top10_path = REPORT_DIR / "top10.json"

    serialized = [
        serialize_item(item)
        for item in results
        if item is not None
    ]

    # -------------------------------------------------
    # Full ranking JSON
    # -------------------------------------------------

    with open(
        json_path,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            serialized,
            f,
            ensure_ascii=False,
            indent=2,
        )

    # -------------------------------------------------
    # TOP10 JSON
    # -------------------------------------------------

    top10 = serialized[:10]

    with open(
        top10_path,
        "w",
        encoding="utf-8",
    ) as f:
        json.dump(
            top10,
            f,
            ensure_ascii=False,
            indent=2,
        )

    # -------------------------------------------------
    # Full ranking CSV
    # -------------------------------------------------

    with open(
        csv_path,
        "w",
        newline="",
        encoding="utf-8",
    ) as f:

        writer = csv.DictWriter(
            f,
            fieldnames=[
                "rank",
                "code",
                "score",
                "final_score",
            ],
            extrasaction="ignore",
        )

        writer.writeheader()

        for item in serialized:

            if not isinstance(item, dict):
                continue

            score = item.get("score")

            writer.writerow(
                {
                    "rank": item.get("rank"),
                    "code": item.get("code"),
                    "score": score,
                    "final_score": item.get(
                        "final_score",
                        score,
                    ),
                }
            )

    return {
        "json": json_path,
        "csv": csv_path,
        "top10": top10_path,
    }