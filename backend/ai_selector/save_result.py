import pandas as pd
from datetime import datetime


def save_top10(top10):

    df = pd.DataFrame(top10)


    filename = (
        "AI_Top10_"
        +
        datetime.now().strftime("%Y%m%d")
        +
        ".csv"
    )


    df.to_csv(

        filename,

        index=False,

        encoding="utf-8-sig"

    )


    print(
        "保存成功:",
        filename
    )


    return filename