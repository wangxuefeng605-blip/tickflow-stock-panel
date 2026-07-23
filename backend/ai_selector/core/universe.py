import akshare as ak
import pandas as pd


def get_a_stock_universe():

    df = ak.stock_info_a_code_name()

    codes = (
        df["code"]
        .astype(str)
        .str.zfill(6)
        .tolist()
    )

    return codes