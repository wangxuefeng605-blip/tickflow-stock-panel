import pandas as pd

from stock_pool import get_stock_pool
from fast_scanner import run_fast_scan
from stock_pool import get_stock_pool
import pandas as pd


def run_ranking():


    stocks=get_stock_pool()


    results=run_fast_scan(
        stocks
    )


    df=pd.DataFrame(results)


    df.sort_values(
        "score",
        ascending=False,
        inplace=True
    )


    df.to_csv(
        "AI_Ranking.csv",
        index=False,
        encoding="utf-8-sig"
    )


    top10=df.head(10)


    top10.to_csv(
        "AI_Top10.csv",
        index=False,
        encoding="utf-8-sig"
    )


    print(top10)





    
    from telegram_bot import send_message



    open(
        "AI_Top10.csv",
        encoding="utf-8"
    ).read()
