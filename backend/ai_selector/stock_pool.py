import pandas as pd
import os
import akshare as ak


POOL_FILE="stock_pool.csv"



def create_stock_pool():

    print("正在重新生成A股股票池...")


    df=ak.stock_info_a_code_name()


    df["code"]=df["code"].astype(str).str.zfill(6)


    #过滤ST
    df=df[
        ~df["name"].str.contains(
            "ST|退",
            na=False
        )
    ]


    df=df[
        [
            "code",
            "name"
        ]
    ]


    df.to_csv(
        POOL_FILE,
        index=False,
        encoding="utf-8-sig"
    )


    print(
        "股票池数量:",
        len(df)
    )


    return df["code"].tolist()



def get_all_stock():

    if os.path.exists(POOL_FILE):

        df=pd.read_csv(
            POOL_FILE,
            dtype={
                "code":str
            }
        )

        if len(df)>1000:

            print(
                "读取本地股票池:",
                len(df)
            )

            return df


    return pd.DataFrame(
        {
            "code":
            create_stock_pool()
        }
    )



def get_stock_pool():

    df=get_all_stock()


    stocks=df["code"].tolist()


    print(
        "最终股票数量:",
        len(stocks)
    )


    return stocks