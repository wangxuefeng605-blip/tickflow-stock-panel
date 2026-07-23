import os
import pandas as pd

RESULT_FILE = "scan_result.csv"
FAILED_FILE = "scan_failed.csv"


# ===========================
# 已完成股票
# ===========================
def load_finished():

    if not os.path.exists(RESULT_FILE):
        return set()

    try:
        df = pd.read_csv(
            RESULT_FILE,
            dtype={"code": str}
        )

        return set(df["code"].astype(str))

    except Exception:
        return set()


# ===========================
# 保存扫描结果
# ===========================
def append_result(rows):

    new = pd.DataFrame(rows)

    if os.path.exists(RESULT_FILE):

        try:

            old = pd.read_csv(
                RESULT_FILE,
                dtype={"code": str}
            )

        except Exception:

            old = pd.DataFrame()

        df = pd.concat(
            [old, new],
            ignore_index=True
        )

    else:

        df = new

    df = df.drop_duplicates(
        subset=["code"],
        keep="last"
    )

    df.to_csv(
        RESULT_FILE,
        index=False,
        encoding="utf-8-sig"
    )


# ===========================
# 保存失败股票
# ===========================
def save_failed(code):

    new = pd.DataFrame(
        [
            {
                "code": str(code)
            }
        ]
    )

    if os.path.exists(FAILED_FILE):

        try:

            old = pd.read_csv(
                FAILED_FILE,
                dtype={"code": str}
            )

        except Exception:

            old = pd.DataFrame(
                columns=["code"]
            )

        df = pd.concat(
            [old, new],
            ignore_index=True
        )

    else:

        df = new

    df = df.drop_duplicates()

    df.to_csv(
        FAILED_FILE,
        index=False,
        encoding="utf-8-sig"
    )