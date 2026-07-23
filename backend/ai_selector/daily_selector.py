import akshare as ak
import pandas as pd
import time

from stock_pool import get_stock_pool
from alpha_factor import alpha_score



def get_history(code):

    try:


        if code.startswith("6"):

            symbol="sh"+code

        else:

            symbol="sz"+code



        df=ak.stock_zh_a_hist_tx(
            symbol=symbol,
            start_date="20250101",
            end_date="20260712"
        )


        if df.empty:
            return None



        df=df.rename(
            columns={
                "date":"date",
                "open":"open",
                "close":"close",
                "high":"high",
                "low":"low",
                "amount":"amount"
            }
        )


        if "volume" not in df.columns:

            df["volume"]=df["amount"]



        return df



    except Exception as e:

        print(
            code,
            "失败",
            e
        )

        return None




def run():


    stocks=get_stock_pool(
        limit=100
    )


    results=[]


    for i,stock in enumerate(stocks):


        code=stock["code"]

        name=stock["name"]


        print(
            f"{i+1}/100",
            code,
            name
        )


        df=get_history(code)


        if df is None:
            continue


        if len(df)<60:
            continue



        score=alpha_score(df)



        results.append(
            {
                "code":code,
                "name":name,
                "score":score
            }
        )


        time.sleep(0.2)



    result=pd.DataFrame(results)


    result=result.sort_values(
        by="score",
        ascending=False
    )


    top10=result.head(10)



    print(
        "\n====== AI TOP10 ======"
    )


    print(top10)



    top10.to_csv(
        "top10_result.csv",
        index=False,
        encoding="utf-8-sig"
    )



if __name__=="__main__":

    run()